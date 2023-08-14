# encoding: utf-8
"""
@project: djangoModel->push_single_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 单挑推送
@created_time: 2023/8/10 10:33
"""
from django.core.paginator import Paginator, EmptyPage
from django.db.models import F

from xj_push.models import PushSingle
from ..orator_models.base_model import base_db
from ..utils.custom_tool import force_transform_type, format_params_handle, filter_fields_handler, write_to_log
from ..utils.j_recur import JRecur


class PushSingleService:
    @staticmethod
    def add(params: dict = None, **kwargs):
        """
        添加推送记录
        :param params: 搜索参数
        :param kwargs: 最省参数
        :return: data, err
        """
        # -------------------------- section 强制类型，字段过滤--------------------------------
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(kwargs)

        try:
            params = format_params_handle(
                param_dict=params, is_validate_type=True,
                filter_filed_list=[
                    "to_user_id|int", "source_code|str", "template_id|int", "template_params|only_dict",
                    "title|str", "content|str", "send_type|str", "files|json"
                ],
            )
            must_keys = ["title", "content", "to_user_id", "send_type"]
            for i in must_keys:
                if not params.get(i):
                    return None, str(i) + " 必填"
        except ValueError as e:
            return None, str(e)
        # -------------------------- section 强制类型，字段过滤 --------------------------------

        # -------------------------- section 构建ORM --------------------------------
        try:
            push_single_record = PushSingle.objects.create(**params)
        except Exception as e:
            write_to_log(prefix="PushSingleService。add:", content=e)
            return None, "插入错误"

        return {"push_single_record": push_single_record.id}, None
        # -------------------------- section 构建ORM --------------------------------

    @staticmethod
    def edit(params: dict = None, **kwargs):
        # -------------------------- section 强制类型，字段过滤--------------------------------
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(kwargs)
        pk, is_pass = force_transform_type(variable=params.get("pk", params.get("id")), var_type="int")
        if not pk:
            return None, "ID错误"
        try:
            params = format_params_handle(
                param_dict=params, is_validate_type=True,
                is_remove_empty=True,
                filter_filed_list=[
                    "to_user_id|int", "source_code|str", "title|str", "content|str",
                    "send_type|str", "files|json", "is_read|int", "is_delete|int",
                    "template_id|int", "template_params|only_dict",
                ]
            )
        except ValueError as e:
            return None, str(e)
        # -------------------------- section 强制类型，字段过滤 --------------------------------

        # -------------------------- section 构建ORM --------------------------------
        # 仅仅查询第一条
        try:
            push_single_record = PushSingle.objects.filter(id=pk)
            if not push_single_record.first():
                return None, "数据不存在，无法修改"
            push_single_record.update(**params)
        except Exception as e:
            write_to_log(prefix="PushSingleService。add:", content=e)
            return None, "插入错误"

        return None, None
        # -------------------------- section 构建ORM --------------------------------

    @staticmethod
    def batch_edit(params: dict = None, search_params: dict = None, **kwargs):
        # -------------------------- section 强制类型，字段过滤--------------------------------
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(kwargs)

        if not search_params:
            search_params, err = JRecur.get_filter_tree_params(
                params=params,
                prefix="search_"
            )

        search_params = format_params_handle(
            param_dict=search_params or {},
            is_validate_type=True,
            is_remove_empty=True,
            filter_filed_list=[
                "to_user_id|int", "source_code|str", "title|str", "content|str",
                "send_type|str", "template_id|int",
            ],
            alias_dict={"title": "title__contains"}
        )
        if not search_params:
            return None, "搜索条件为空"

        try:
            params = format_params_handle(
                param_dict=params, is_validate_type=True,
                is_remove_empty=False,
                filter_filed_list=[
                    "to_user_id|int", "source_code|str", "title|str", "content|str",
                    "send_type|str", "files|json", "is_read|int", "is_delete|int",
                    "template_id|int", "template_params|only_dict",
                ]
            )
        except ValueError as e:
            return None, str(e)
        # -------------------------- section 强制类型，字段过滤 --------------------------------

        # -------------------------- section 构建ORM --------------------------------
        # 仅仅查询第一条
        print("params", params)
        print("search_params", search_params)
        try:
            push_single_record = PushSingle.objects.filter(**search_params)
            push_single_record.update(**params)
        except Exception as e:
            write_to_log(prefix="PushSingleService。add:", content=e)
            return None, "插入错误"

        return None, None
        # -------------------------- section 构建ORM --------------------------------

    @staticmethod
    def delete(params: dict = None, **kwargs):
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(kwargs)
        pk, is_pass = force_transform_type(variable=params.get("pk") or params.get("id"), var_type="int")
        if not pk:
            return None, "ID不能为空"
        push_single_record = PushSingle.objects.filter(id=pk).first()
        if push_single_record:
            push_single_record.delete()
        return None, None

    @staticmethod
    def list(params: dict = None, filter_fields: "list|str" = None, only_first: bool = False, need_pagination: bool = True, **kwargs):
        """
        单挑推送记录
        :param params: 搜索参数
        :param filter_fields: 过滤字段
        :param only_first: 是否仅仅查询第一条
        :param need_pagination: 是否分页
        :param kwargs: 最省参数
        :return: data, err
        """
        # -------------------------- section 强制类型 --------------------------------
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(kwargs)
        size, is_pass = force_transform_type(variable=params.pop('size', 10), var_type="int", default=10)
        page, is_pass = force_transform_type(variable=params.pop('page', 1), var_type="int", default=1)
        # -------------------------- section 强制类型 --------------------------------

        # -------------------------- section 参数过滤 --------------------------------
        # 允许查询字段过滤
        params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "id|int", "to_user_id|int", "source_code|str", "title|str", "content|str",
                "send_type|str", "files|json", "is_read|int", "is_delete|int",
                "created_time_start|date", "created_time_end|date",
            ],
            alias_dict={"created_time_start": "created_time__gte", "created_time_end": "created_time__lte"}
        )
        # 处理filter_fields，获取ORM查询字段列表
        filter_fields_list = filter_fields_handler(
            input_field_expression=filter_fields,
            all_field_list=[
                "id", "to_user_id", "source_code", "title", "content", "template_id", "template_params", "template_template",
                "send_type", "files", "is_read", "is_delete", "created_time"
            ]
        )
        # -------------------------- section 参数过滤 --------------------------------

        # -------------------------- section 构建ORM --------------------------------
        push_single_record = PushSingle.objects.annotate(
            template_template=F("template__template")
        ).filter(**params).values(*filter_fields_list)

        # 仅仅查询第一条
        if only_first:
            push_single_record = push_single_record.first()
            push_single_record["template_msg"] = push_single_record["template_template"]
            for k, v in push_single_record.get("template_params").items():
                push_single_record["template_msg"] = push_single_record["template_msg"].replace("{" + k + "}", v)
            return push_single_record, None

        # 不分页查询
        total = push_single_record.count()
        if not need_pagination and total <= 200:
            finish_list = list(push_single_record)
            return finish_list, None

        # 分页查询
        paginator = Paginator(push_single_record, size)
        try:
            enroll_obj = paginator.page(page)
        except EmptyPage:
            return {'total': total, "page": page, "size": size, 'list': []}, None
        except Exception as e:
            return None, f'{str(e)}'
        finish_list = list(enroll_obj.object_list)

        # 替换钼靶变量
        for i in finish_list:
            i["template_msg"] = i["template_template"]
            if not i.get("template_template") or not i.get("template_params"):
                continue
            for k, v in i.get("template_params").items():
                i["template_msg"] = i["template_msg"].replace("{" + k + "}", v)

        return {'total': total, "page": page, "size": size, 'list': finish_list}, None
        # -------------------------- section 构建ORM --------------------------------

    @staticmethod
    def group_list(params: dict = None, filter_fields: "list|str" = None, only_first: bool = False, need_pagination: bool = True, **kwargs):
        """
        单挑推送分组查询记录
        :param params: 搜索参数
        :param filter_fields: 过滤字段
        :param only_first: 是否仅仅查询第一条
        :param need_pagination: 是否分页
        :param kwargs: 最省参数
        :return: data, err
        """
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(kwargs)

        # 参数处理
        size, is_pass = force_transform_type(variable=params.pop('size', 10), var_type="int", default=10)
        page, is_pass = force_transform_type(variable=params.pop('page', 1), var_type="int", default=1)
        source_code, is_pass = force_transform_type(variable=params.get("source_code"), var_type="str", default={})

        # 构建ORM
        query_set = base_db.table("push_single").select_raw("""
            to_user_id,
            source_code,
            title,
            content,
            template_id,
            template_params,
            send_type,
            files,
            is_read,
            is_delete,
            count(id) as total,
            date_format(created_time, "%%Y-%%m-%%d %%H:%%m:%%s") as created_time
        """).group_by("source_code")

        total_query = base_db.table("push_single").select_raw("count( DISTINCT source_code ) as total")
        if source_code:
            query_set = query_set.where("source_code", "=", source_code)
            total_query = total_query.where("source_code", "=", source_code)
        query_set = query_set.order_by("created_time", "desc").paginate(size, page)

        # 汇总查询
        total = total_query.pluck("total")
        un_read_total = base_db.table("push_single").select_raw("count(id) as un_read_total").where("is_read", 0).pluck("un_read_total")
        un_read_total_map = base_db.table("push_single").select_raw("""
            source_code,
            count(id) as un_read_total
        """).where("is_read", 0).where_in("source_code", [i["source_code"] for i in query_set]).group_by("source_code").lists("un_read_total", "source_code")

        for i in query_set:
            i["un_read_total"] = un_read_total_map.get(i["source_code"], 0)

        return {"page": page, "size": size, "total": total, "un_read_total": un_read_total, "list": list(query_set)}, None
