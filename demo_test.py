#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import pymongo
import streamlit as st
from streamlit_ace import st_ace

INITIAL_CODE = """#print()打印信息在当前页面不会显示
#代码段内的print()请使用st.text()替代打印输出
#需要的返回值自行定义一个变量,接收后统一返回，建议使用字典,方便后续取用
#example：
return_info={}
def main_1():
    a_list=["value"] 
    return a_list
return_info['a_list']=main_1()
st.text(f"自定义返回结果集如下{return_info}")
"""
# PAGE_SETTING
st.set_page_config(
    page_title="Stream_app_demo_V1",
    page_icon="🎆🎇💥🤩",
    layout="wide",
    initial_sidebar_state="expanded",
)


# def test(*args,**kwargs):
#     pass
def main_edit_python():
    code = st_ace(
        value=INITIAL_CODE,
        language="python",
        placeholder="st.text('Hello world!')",
        # theme="solarized_light",
        theme="idle_fingers",
        keybinding="vscode",
        font_size=14,
        tab_size=4,
        wrap=True,
        show_gutter=True,
        auto_update=False,
        readonly=False,
        key="ace_editor",
        height=400,
        show_print_margin=False,
    )
    return code


# def main():
#     c1, c2 = st.columns([3, 1])
#
#     c2.subheader("Parameters")
#
#     with c1:
#         content = st_ace(
#             placeholder=c2.text_input("Editor placeholder", value="Write your code here"),
#             language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
#             theme=c2.selectbox("Theme", options=THEMES, index=35),
#             keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
#             font_size=c2.slider("Font size", 5, 24, 14),
#             tab_size=c2.slider("Tab size", 1, 8, 4),
#             show_gutter=c2.checkbox("Show gutter", value=True),
#             show_print_margin=c2.checkbox("Show print margin", value=False),
#             wrap=c2.checkbox("Wrap enabled", value=False),
#             auto_update=c2.checkbox("Auto update", value=False),
#             readonly=c2.checkbox("Read-only", value=False),
#             min_lines=45,
#             key="ace",
#         )
#
#         if content:
#             st.subheader("Content")
#             st.text(content)
#             st.subheader("执行结果")
#             ssss = eval('content')
#             myList = [item for item in ssss.replace('\n', ' ')]
#             aim_res = ''.join(myList)
#             # aim_res = str(ssss.replace('\n',''))
#             print(aim_res)
#             test_code = compile(ssss, '', 'exec')
#             xxxx = """def test(): aa=11+22 return aa"""
#             ccccc = eval('aim_res')
#             print(ccccc)
#             st.text(ccccc)


# SIDEBAR
st.sidebar.selectbox("你的选择项", ["list1", "list2"])
# LINE1
st.write("line1布局")
aim_host = "http://10.3.1.64:5000/"
api_dict = {}
api_dict["test4"] = {"get": "", "description": "测试服务接口"}
api_dict["test1"] = {"get": "?name=111", "description": "测试服务接口"}
api_dict["test2"] = {"post": {"age": "25", "name": "你的名字"}, "description": "用户注册接口"}
api_dict["test3"] = {"post": {"name": "你好", "age": 25}, "description": "测试"}

# st.write(api_dict)
# 展示API 接口的详细数据
# st.write(len(api_dict.items()), api_dict.items())
# 遍历API的键,即接口地址
api_url_list = list(api_dict.keys())
host = st.text_input('##HOST地址', aim_host, help="全局请求的host地址，根据不同部署环境自行填写")
# LINE2
layout_left, layout_right = st.columns([2, 2])
with layout_left:
    "line2_LEFT"
    form_headers = st.form("form_headers")
    form_body = st.form("form_body")
with layout_right:
    "line2_RIGHT"
    form_response = st.form("form_response")

with form_headers:
    st.write("headers")
    form_headersheaders_submit = form_headers.form_submit_button("headers_submit")
with form_body:
    st.write("body")
    with st.expander(label="点击查看代码块 编码规范帮助", expanded=False):
        st.code("""#print()打印信息在当前页面不会显示\
#代码段内的print()请使用st.text()替代打印输出
#需要的返回值自行定义一个变量,接收后统一返回，建议使用字典,方便后续取用
#example：报错model不存在，请联系管理员添加。xxx@mail.com
return_info={}
def main_1():
    a_list=["value"]
    return a_list
return_info['a_list']=main_1()
st.text(f"自定义返回结果集如下{0}".format(return_info))
    """, language="python")
    with st.expander(label="Edit Python Code 点击展开"):
        # st.write('##### Code editor')
        code_aim = main_edit_python()

        st.write('Hit `CTRL+ENTER` to refresh and save your code separately')
        st.write('*点击body_submit执行代码*')
    body_submit = st.form_submit_button("body_submit")

    # st.write(code)

with form_response:
    st.write("response")
    res_input = st.text_input("请输入")
    response_submit = st.form_submit_button("response_submit", on_click=None)
    if response_submit:
        st.write(res_input)
        st.balloons()
my_expander = st.expander(label="ddd")
my_expander.write('Hello there!')
clicked = my_expander.button('Click me!')

# res = requests.get("https://www.baidu.com")
# st.write(res.request.headers)
with layout_right:
    # try:
    #     # exec(code)
    #     with st.expander(label="被执行的代码块内容", expanded=True):
    #         st.code(code, language="python")
    #         eval(str(code))
    # except OSError as e:
    #     if "Invalid argument: '<string>'" in str(e):
    #         pass
    #     else:
    #         st.exception(e)
    # else:
    #     if body_submit:
    #         st.write("# *edit python 执行结束* #")
    with st.expander(label="被执行的代码块内容", expanded=True):
        st.code(code_aim, language="Python")
        # str_code = compile(code_aim, '', 'exec')
        # aim_code=str_code
        # edit_code=getattr(aim_code,"a_list")
        # st.text(str_code)
        # print("code_return\n", type(code_return),code_return)

    if body_submit:
        with st.expander(label="代码块输出结果", expanded=True):
            # compile(code_aim, '', 'exec')
            exec(code_aim)
            code_run = code_aim.split('def')
            code_main = code_run[1].rsplit('():')[0].lstrip()

            code_return = eval(code_main)()
        st.write("# *edit python 执行结束* #")
        # code_return = exec("test(code=str_code)")
        st.write("code_return", code_return)

# 复制展示内容
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
# 复制展示内容
# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

# Pull data from the collection.
# Uses st.cache to only rerun when the query changes or after 10 min.
search_db = "aa"
mycollection = search_db


@st.cache(ttl=600)
def get_data():
    db = client.aa
    items = db.aa.find()
    items = list(items)  # make hashable for st.cache
    return items


items = get_data()
# with st.expander('json数据展示'):
#     st.write(items)
with st.container():
    st.write(items)
# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['age']}:")
# st.set_option("magicEnabled", "false")
# st.write(exec(expr))
dict_check = st.checkbox("Data Dictionary")
# dict_markdown = read_markdown_file("data_dictionary.md")

if dict_check:
    st.write("你好")


def get_user_name():
    return 'John'


with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'


    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

    # And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
option = st.sidebar.selectbox(
    'Which number do you like best?',
    ['first column', '22'])

st.sidebar.write('You selected:', option)
# st.container()
# st.columns(spec=2)
col1, col2 = st.columns(2)

with st.container():
    st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))
st.balloons()
with col1.subheader('Columnisation'):
    with st.expander('Expander', expanded=True):
        st.write('col1')

with col2.subheader('AAAAAAAAAAAAAA'):
    with st.expander('Expand'):
        st.write('Juicy deets')
st.write("This is outside the container")
