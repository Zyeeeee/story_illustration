import streamlit as st
from io import BytesIO
from PIL import Image
from openai import OpenAI
import image_process
client = OpenAI(
    base_url='https://external.api.recraft.ai/v1',
    api_key='VaF63vGlp9sG59dKUccGx4Gx3XXjKkECM8VriJ2LQV9NdJznH5iQ9h85z8fRybKl',
) # 

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
    st.caption("增加了图片大小处理，极大的减少了图片尺寸不正确的错误率，但不是特别完善，不能保证100%处理完全，如果出错请重新上传一张别的图片，我敢保证不是代码的问题✨")
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
        "荷兰郁金香🌷": {
            "prompts": [
                "A painting of a hand-painted cute style cat is holding a brush in its hand. Buckets of paint lay on the floor. The cat is standing under a big white windmill tower with some pigments on it.In the background is a spectacular tulip field. Watercolor style.",
                "A painting of a hand-painted cute style cat trying to catch a bee in the sky. Next to the cat is an overturned paint bucket with the yellow paint spilled all over the floor. The background is a spectacular tulip field. Watercolor style."
            ],
            "controls": [
                {'colors': [{'rgb': [215, 226, 234]}, {'rgb': [183, 208, 222]}, {'rgb': [197, 216, 227]},{'rgb': [158, 203, 226]}, {'rgb': [244, 38, 36]}, {'rgb': [242, 7, 18]},{'rgb': [116, 89, 70]}, {'rgb': [248, 82, 59]},{'rgb':[250, 247, 117]}], 'background_color': {'rgb': [176, 218, 247]}, 'no_text': True},
                {'colors': [{'rgb': [215, 226, 234]}, {'rgb': [183, 208, 222]}, {'rgb': [197, 216, 227]},{'rgb': [158, 203, 226]}, {'rgb': [244, 38, 36]}, {'rgb': [242, 7, 18]},{'rgb': [116, 89, 70]}, {'rgb': [248, 82, 59]}, {'rgb': [250, 247, 117]}], 'background_color': {'rgb': [176, 218, 247]}, 'no_text': True}
            ],
            "description": "在郁金香海里，沉稳小黑用尾巴蘸取洒落的颜料在风车上作画，莽撞小白追蜜蜂时撞翻颜料桶。"
        },
        "霍比特村里的🐱": {
            "prompts": [
                "A painting of a hand-painted cute style cat walking in the Hobbit Village",
                "A painting of a hand-painted cute style cat holding a cod pie in a hobbit house"
            ],
            "controls": [
                {'no_text': True},
                {'no_text': True}
            ],
            "description": "两只猫咪在霍比特村的绿丘上玩耍，小黑无意间钻进了一个霍比特小屋的窗户里。小白在外面焦急地踱步，结果没多久，小黑叼着一块刚出炉的派探头出来，得意地朝小白晃了晃。小白无奈地叹口气，伸出爪子接住派，心照不宣地一起躲到草丛里享用美食。"
        },
        "九寨沟国家公园💦": {
            "prompts": [
                "A painting of a hand-painted cute style cat watching a school of small fish swimming in a lake. The cat is sitting on a rock near a pond, with a natural landscape featuring a calm clear karst lake in the background. There is a reflection of the cat on the water. The background is a crystal clear Karst landform lake. A digital illustration in a watercolor style",
                "A painting of a hand-painted cute style cat running on the shore of the lake with a fish hold in its mouth. The cat is running on the rocks near a lake, with a natural landscape featuring a calm clear karst lake in the background. There is a reflection of the cat on the water. The background is a crystal clear Karst landform lake. A digital illustration in a watercolor style"
            ],
            "controls": [
                {'colors': [{'rgb': [83, 189, 160]}, {'rgb': [85, 149, 117]}, {'rgb': [98, 173, 142]},{'rgb': [46, 120, 116]}, {'rgb': [33, 142, 111]},{'rgb': [87, 201, 233]},{'rgb': [98, 203, 214]}, {'rgb': [207, 236, 144]}], 'background_color': {'rgb': [136, 240, 237]}, 'no_text': True},
                {'colors': [{'rgb': [83, 189, 160]}, {'rgb': [85, 149, 117]}, {'rgb': [98, 173, 142]},{'rgb': [46, 120, 116]}, {'rgb': [33, 142, 111]},{'rgb': [87, 201, 233]},{'rgb': [98, 203, 214]}, {'rgb': [207, 236, 144]}], 'background_color': {'rgb': [136, 240, 237]}, 'no_text': True}
            ],
            "description": "在清澈碧绿的湖水边，小白正在低头观察湖水中的小鱼，伸手想把水里的鱼捞起来。一转头，在一枝横在湖面上的枯树上，小黑嘴里叼着鱼在狭窄的枯枝上奔跑，准备和小白分享他的战利品。"
        },
        "哈尔滨冰雪大世界🛝": {
            "prompts": [
                "A painting of a hand-painted cute style cat sliding down a ice slide in Harbin Ice and Snow World. The cat is resting on a sled-like object on a snowy surface. The background consists of a wintry landscape with snow-covered slopes and frost-covered structures inspired by igloos.",
                "A painting of a hand-painted cute style cat at the entrance of an ice slide looked at the long slide and was afraid to go down. The background consists of a wintry landscape with snow-covered slopes and frost-covered structures inspired by ice castle. "
            ],
            "controls": [
                {'background_color': {'rgb': [255, 255, 255]}, 'no_text': True},
                {'background_color': {'rgb': [255, 255, 255]}, 'no_text': True}
            ],
            "description": "两只小猫去冰雪大世界玩，小白在长滑梯口不敢滑下去，小黑咻地勇敢、开心滑了下去"
        },
        "洱海海鸥🐦": {
            "prompts": [
                "A painting of a hand-painted cute style cat attacked a seagull resting on a dead tree beside Erhai Lake. The seagull stood on the dead tree, and the cat held out a paw towards the seagull.In the background, Erhai Lake meets sky and water and some dead trees Illustrations of lovely children's hand-drawn style.",
                "A painting of a hand-painted cute style cat being chased by a seagull in Erhai. The cat was running and the seagulls were attacking the cat's head.In the background, Erhai Lake meets sky and water and some dead trees. Illustrations of children's hand-drawn style. "
            ],
            "controls": [
                {'colors': [{'rgb': [85, 166, 216]}, {'rgb': [105, 177, 219]}, {'rgb': [125, 183, 219]},{'rgb': [79, 109, 137]}, {'rgb': [143, 190, 223]},{'rgb': [96, 125, 151]},{'rgb': [71, 146, 182]}, {'rgb': [113, 137, 159]}, {'rgb': [175, 208, 226]}], 'background_color': {'rgb': [152, 204, 241]}, 'no_text': True},
                {'colors': [{'rgb': [85, 166, 216]}, {'rgb': [105, 177, 219]}, {'rgb': [125, 183, 219]},{'rgb': [79, 109, 137]}, {'rgb': [143, 190, 223]},{'rgb': [96, 125, 151]},{'rgb': [71, 146, 182]}, {'rgb': [113, 137, 159]}, {'rgb': [175, 208, 226]}], 'background_color': {'rgb': [152, 204, 241]}, 'no_text': True}
            ],
            "description": "小黑看到一只海鸥停在枯树上休息，露出淘气的神情，悄悄爬上树，准备偷袭海鸥。就在它扑过去的一瞬间，海鸥灵巧地飞起，躲过了攻击。而小白正好站在树下看热闹，没想到那只被惊扰的海鸥直接飞下来，对着小白的脑壳“啄”了一下，吓得小白“喵”地一声跳了起来。小黑在树上笑得直打滚，小白气得追着小黑跑：“都怪你！害我被啄了！”"
        },
        "可可西里的🐐和🐱": {
            "prompts": [
                "A painting of a hand-painted cute style cat sleeping on the grassland under a snowy mountain. There's a herd of antelope grazing in the back. The snowy mountains of Hoh Xil stretch in the background.Blue sky and white clouds",
                "A hand-painted cute style digital illustration featuring a cat runs towards a herd of antelopes on the grassland under a snowy mountain. The antelopes are frightened and run away. The snowy mountains of Hoh Xil stretch in the background.Blue sky and white clouds"
            ],
            "controls": [
                {'colors': [{'rgb': [86, 138, 201]}, {'rgb': [174, 176, 202]}, {'rgb': [132, 157, 205]},{'rgb': [154, 165, 202]}, {'rgb': [235, 238, 242]},{'rgb': [112, 146, 200]},{'rgb': [182, 236, 128]}, {'rgb': [255, 255, 255]}], 'no_text': True},
                {'colors': [{'rgb': [86, 138, 201]}, {'rgb': [174, 176, 202]}, {'rgb': [132, 157, 205]},{'rgb': [154, 165, 202]}, {'rgb': [235, 238, 242]},{'rgb': [112, 146, 200]},{'rgb': [182, 236, 128]}, {'rgb': [255, 255, 255]}], 'no_text': True}
            ],
            "description": "雪山前的草原上一群羚羊正在悠闲吃草，小黑一个箭步跃羚羊的背上，羚羊温顺地驮着小黑，小黑耳朵被风吹得一抖一抖，眼睛眯成了一条线，享受着这独特的“羚羊快车”。疲惫的小白靠着羚羊在呼呼大睡。"
        },
        "峨眉山的🐒和🐱": {
            "prompts": [
                "A hand-painted cute style digital illustration featuring a cat carrying a schoolbag and a monkey on a wooden deck overlooking a mountainous landscape.The cat is running  in the foreground, and the monkey, with a smaller size and a simple green accessory, is positioned slightly behind the cat. The deck has a rustic appearance with wooden planks and a simple railing.  The background consists of lush greenery and a series of mountains  shrouded in clouds fading into the distance. ",
                "A hand-painted cute style digital illustration featuring a cat throwing stones at a monkey in a tree on Mount Emei. a brown monkey on a tree branch, and a lush, natural environment with greenery and mountains in the background. The cat is sitting on a rock-like formation in the foreground, while the monkey is perched on a tree branch above. The background consists of a range of greenery and rolling hills shrouded in clouds."
            ],
            "controls": [
                {'no_text': True},
                {'no_text': True}
            ],
            "description": "雪山前的草原上一群羚羊正在悠闲吃草，小黑一个箭步跃羚羊的背上，羚羊温顺地驮着小黑，小黑耳朵被风吹得一抖一抖，眼睛眯成了一条线，享受着这独特的“羚羊快车”。疲惫的小白靠着羚羊在呼呼大睡。"
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