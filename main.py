import streamlit as st
from io import BytesIO
from PIL import Image
from openai import OpenAI
import image_process
client = OpenAI(
    base_url='https://external.api.recraft.ai/v1',
    api_key='VaF63vGlp9sG59dKUccGx4Gx3XXjKkECM8VriJ2LQV9NdJznH5iQ9h85z8fRybKl',
)

def call_recraft_api(image1, prompt, controls):
    # image1 = Image.open(image_file)

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
        },
        "🆕荷兰郁金香🌷": {
            "prompts": [
                "A painting of a hand-painted cute style cat is holding a brush in its hand. Buckets of paint lay on the floor. The cat is standing under a big white windmill tower with some pigments on it.In the background is a spectacular tulip field. Watercolor style.",
                "A painting of a hand-painted cute style cat trying to catch a bee in the sky. Next to the cat is an overturned paint bucket with the yellow paint spilled all over the floor. The background is a spectacular tulip field. Watercolor style."
            ],
            "controls": [
                {'colors': [{'rgb': [215, 226, 234]}, {'rgb': [183, 208, 222]}, {'rgb': [197, 216, 227]},
                            {'rgb': [158, 203, 226]}, {'rgb': [244, 38, 36]}, {'rgb': [242, 7, 18]},
                            {'rgb': [116, 89, 70]}, {'rgb': [248, 82, 59]},{'rgb':[250, 247, 117]}]
                            , 'background_color': {'rgb': [176, 218, 247]}, 'no_text': True},
                {'colors': [{'rgb': [215, 226, 234]}, {'rgb': [183, 208, 222]}, {'rgb': [197, 216, 227]},
                            {'rgb': [158, 203, 226]}, {'rgb': [244, 38, 36]}, {'rgb': [242, 7, 18]},
                            {'rgb': [116, 89, 70]}, {'rgb': [248, 82, 59]}, {'rgb': [250, 247, 117]}]
                            , 'background_color': {'rgb': [176, 218, 247]}, 'no_text': True}
            ],
            "description": "在郁金香海里，沉稳小黑用尾巴蘸取洒落的颜料在风车上作画，莽撞小白追蜜蜂时撞翻颜料桶。"
        },
        "🆕霍比特村里的🐱": {
            "prompts": [
                "A painting of a hand-painted cute style cat walking in the Hobbit Village",
                "A painting of a hand-painted cute style cat holding a cod pie in a hobbit house"
            ],
            "controls": [
                {'no_text': True},
                {'no_text': True}
            ],
            "description": "两只猫咪在霍比特村的绿丘上玩耍，小黑无意间钻进了一个霍比特小屋的窗户里。小白在外面焦急地踱步，结果没多久，小黑叼着一块刚出炉的派探头出来，得意地朝小白晃了晃。小白无奈地叹口气，伸出爪子接住派，心照不宣地一起躲到草丛里享用美食。"
        }
    }

    selected_category = st.selectbox("选一个故事模板", list(categories.keys()))
    prompts = categories[selected_category]["prompts"]
    controls = categories[selected_category]["controls"]
    description = categories[selected_category]["description"]

    # 显示选中的模板描述
    st.write(f"故事描述: {description}")

    col1, col2 = st.columns(2)
    with col1:
        image1 = st.file_uploader("第一张猫图", type=["png", "jpg", "jpeg"], key="image1")
        if image1 is not None:
            st.image(image1, caption="原图",use_container_width=True)
            image = Image.open(image1)
            image1 = image_process.blur_image(image)
    with col2:
        image2 = st.file_uploader("第二张猫图", type=["png", "jpg"], key="image2")
        if image2 is not None:
            st.image(image2, caption="原图",use_container_width=True)
            image = Image.open(image2)
            image2 = image_process.blur_image(image)

    if st.button("开始炼丹"):
        if image1 and image2:
            col1, col2 = st.columns(2)
            with col1:
                st.image(image1, caption="4:3并高斯模糊", use_container_width=True)
            with col2:
                st.image(image2, caption="4:3并高斯模糊", use_container_width=True)

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

    st.write("想一次生成多个模板？在下面勾选你想要的故事模板 ⬇️")

    # 添加分割线
    st.markdown("---")
    st.subheader("多模板生成")

    # 创建每个模板的勾选框
    selected_templates = {}
    for category in categories.keys():
        selected_templates[category] = st.checkbox(f"{category} - {categories[category]['description']}")

    # ProMax 模式：运行用户勾选的模板
    if st.button("炼丹promax（生成已勾选的模板）"):
        if image1 and image2:
            # 检查是否至少选择了一个模板
            if any(selected_templates.values()):
                st.write("正在生成选中的模板...")

                # 逐个处理选中的模板
                results = {}
                for category, selected in selected_templates.items():
                    if selected:
                        st.write(f"正在生成 {category} 模板...")

                        # 获取当前模板的提示和控制参数
                        template_prompts = categories[category]["prompts"]
                        template_controls = categories[category]["controls"]

                        # 调用API生成图片
                        results[category] = {
                            "img1": call_recraft_api(image1, template_prompts[0], template_controls[0]),
                            "img2": call_recraft_api(image2, template_prompts[1], template_controls[1])
                        }

                # 显示所有生成的图片
                for category, images in results.items():
                    st.markdown(f"### {category}")
                    if images["img1"] and images["img2"]:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.image(images["img1"], caption=f"Redrawn Image 1 ({category})", use_container_width=True)
                        with col2:
                            st.image(images["img2"], caption=f"Redrawn Image 2 ({category})", use_container_width=True)
                    else:
                        st.error(f"生成 {category} 模板的图片失败")
            else:
                st.warning("请至少选择一个模板")
        else:
            st.error("叫你上传两张图不听是吧")



if __name__ == "__main__":
    main()