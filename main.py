import streamlit as st
import requests
from io import BytesIO
from PIL import Image
from openai import OpenAI

client = OpenAI(
    base_url='https://external.api.recraft.ai/v1',
    api_key='VaF63vGlp9sG59dKUccGx4Gx3XXjKkECM8VriJ2LQV9NdJznH5iQ9h85z8fRybKl',
)

def call_recraft_api(image_file, prompt, controls):
    image1 = Image.open(image_file)

    # 在内存中转换为 PNG 格式
    image1_png = BytesIO()
    image1.save(image1_png, format='PNG')
    image1_png.seek(0)  # 将指针重置到缓冲区开头
    response1 = client.post(
        path='/images/imageToImage',
        cast_to=object,
        options={'headers': {'Content-Type': 'multipart/form-data'}},
        files={
            'image': ('image.png', image1_png, 'image/png')
        },
        body={
            'prompt': prompt,
            'strength': 0.66,
            'controls': controls
        },
    )
    return response1['data'][0]['url']


def main():
    st.title("故事插图体体体体验")
    st.write("体验现有的故事插图（现有的意思是我现在做好有的）")

    # 定义栏目和对应的 prompts
    categories = {
        "梯田春游🌱": {
            "prompts":[
            "A painting of a hand-painted cute style of a cat and a lovely straw-made man. They are standing on a green field. The man is smiling. The cat is reaching out his hand for the man's hat.The background is a terraced fields with some small yellow flowers. ",
            "A painting of a hand-painted cute style. A cat is carrying a flower in its mouth and walking on green field. The background is a green terraced fields with some small yellow flowers."
        ],
        "controls":[
            {'background_color': {'rgb': [59, 209, 77]}, 'no_text' : True},
            {'background_color': {'rgb': [59, 209, 77]}, 'no_text' : True}
        ],
        "description":"两咪春天去在田野边春游，在田野边上见到一个稻草人，小白把自己的帽子戴在稻草人头上，小黑叼了一朵花准备送给稻草人"
        },
        "哈尔滨❄️": {
            "prompts":[
            "A painting of a hand-painted cute style cat is being hit by some flying snowballs. The cat is having a snowball fight and was hit with a lot of snow. The background is a snowy scene with a snowman in the snow.Outside.",
            "A painting of a hand-painted cute style cat is throwing snowballs and having a snowball fight. The cat is in a dynamic motion of throwing some snowballs. Many snowballs lying around. The background is a snowy scene.Outside."
        ],
        "controls":[
            {'background_color': {'rgb': [255, 255, 255]}, 'no_text' : True},
            {'background_color': {'rgb': [255, 255, 255]}, 'no_text' : True}
        ],
        "description": "两咪去哈尔滨当小土豆，第一次看到雪很开心，小黑兴冲冲去堆雪人，小白使坏拿雪球砸向堆雪人的小黑，小黑被砸后哈哈大笑，也加入了打雪仗当中 "
        },
        "东京🌸": {
            "prompts": [
                "A painting of a hand-painted cute style cat. Sitting on the top of a tram looking at many cherry blossoms. There are many pink petals scattered on and around the cat, and pink petals are falling in the sky.",
                "A painting of a hand-painted cute style cat. Sitting on the top of a tram looking at many cherry blossoms. There are many pink petals scattered on and around the cat, and pink petals are falling in the sky."
            ],
            "controls": [
                {'colors':[{'rgb':[177,114,117]},{'rgb':[164,97,99]},{'rgb':[194,137,142]},{'rgb':[204,153,157]},{'rgb':[184,128,132]},{'rgb':[126,170,207]},{'rgb':[220,184,187]},{'rgb':[158,189,220]},{'rgb':[206,169,173]},{'rgb':[102,66,65]}], 'background_color': {'rgb': [126, 172, 212]}, 'no_text': True},
                {'colors':[{'rgb':[177,114,117]},{'rgb':[164,97,99]},{'rgb':[194,137,142]},{'rgb':[204,153,157]},{'rgb':[184,128,132]},{'rgb':[126,170,207]},{'rgb':[220,184,187]},{'rgb':[158,189,220]},{'rgb':[206,169,173]},{'rgb':[102,66,65]}], 'background_color': {'rgb': [126, 172, 212]}, 'no_text': True}
            ],
        "description": "两猫趴在电车顶看樱花，小黑突然跃起摇晃树枝，粉色花瓣雨般落在小白猫身上。小白猫气鼓鼓抖毛。"
        }
    }

    selected_category = st.selectbox("选一个故事模板", list(categories.keys()))
    prompts = categories[selected_category]["prompts"]
    controls = categories[selected_category]["controls"]
    description = categories[selected_category]["description"]

    # 显示选中的模板描述
    st.write(f"模板描述: {description}")

    col1, col2 = st.columns(2)
    with col1:
        image1 = st.file_uploader("第一张猫图", type=["png", "jpg"], key="image1")
    with col2:
        image2 = st.file_uploader("第二张猫图", type=["png", "jpg"], key="image2")

    if st.button("开始炼丹"):
        if image1 and image2:
            col1, col2 = st.columns(2)
            with col1:
                st.image(image1, caption="Original Image 1", use_container_width=True)
            with col2:
                st.image(image2, caption="Original Image 2", use_container_width=True)

            st.write("在做了在做了")

            redrawn1 = call_recraft_api(image1, prompts[0], controls[0])
            redrawn2 = call_recraft_api(image2, prompts[1], controls[1])

            if redrawn1 and redrawn2:
                col1, col2 = st.columns(2)
                with col1:
                    st.image(redrawn1, caption="Redrawn Image 1", use_container_width=True)
                with col2:
                    st.image(redrawn2, caption="Redrawn Image 2", use_container_width=True)
        else:
            st.error("叫你上传两张图不听是吧")
    st.write("一次一个不够爽？试试下面这个按钮⬇️")
    # ProMax 模式：一次性跑三个模板
    if st.button("炼丹promax（现有模板全都跑）"):
        if image1 and image2:
            st.write("你是会烧钱的💰👍")
            st.write("正在生成三个模板...")

            # 生成第一个模板
            redrawn1 = call_recraft_api(image1, categories["梯田春游🌱"]["prompts"][0], categories["梯田春游🌱"]["controls"][0])
            redrawn2 = call_recraft_api(image2, categories["梯田春游🌱"]["prompts"][1], categories["梯田春游🌱"]["controls"][1])

            # 生成第二个模板
            redrawn3 = call_recraft_api(image1, categories["哈尔滨❄️"]["prompts"][0], categories["哈尔滨❄️"]["controls"][0])
            redrawn4 = call_recraft_api(image2, categories["哈尔滨❄️"]["prompts"][1], categories["哈尔滨❄️"]["controls"][1])

            # 生成第三个模板
            redrawn5 = call_recraft_api(image1, categories["东京🌸"]["prompts"][0], categories["东京🌸"]["controls"][0])
            redrawn6 = call_recraft_api(image2, categories["东京🌸"]["prompts"][1], categories["东京🌸"]["controls"][1])

            if redrawn1 and redrawn2 and redrawn3 and redrawn4 and redrawn5 and redrawn6:
                col1, col2 = st.columns(2)
                with col1:
                    st.image(redrawn1, caption="Redrawn Image 1 (梯田春游🌱)", use_container_width=True)
                with col2:
                    st.image(redrawn2, caption="Redrawn Image 2 (梯田春游🌱)", use_container_width=True)

                col3, col4 = st.columns(2)
                with col3:
                    st.image(redrawn3, caption="Redrawn Image 1 (哈尔滨❄️)", use_container_width=True)
                with col4:
                    st.image(redrawn4, caption="Redrawn Image 2 (哈尔滨❄️)", use_container_width=True)

                col5, col6 = st.columns(2)
                with col5:
                    st.image(redrawn5, caption="Redrawn Image 1 (东京🌸)", use_container_width=True)
                with col6:
                    st.image(redrawn6, caption="Redrawn Image 2 (东京🌸)", use_container_width=True)
        else:
            st.error("叫你上传两张图不听是吧")



if __name__ == "__main__":
    main()