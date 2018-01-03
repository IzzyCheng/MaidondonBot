from transitions import State
from transitions.extensions import GraphMachine
import telegram

money = 0
API_TOKEN = '512230103:AAHXXTpd6PenKbPMY5E1nBu1RpY9XWSUURw'
bot = telegram.Bot(token=API_TOKEN)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text == '嗨'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text == '超值全餐'

    def is_going_to_state5(self, update):
        text = update.message.text
        global money
        if text == '1':
            money += 69
        elif text == '2':
            money += 59
        elif text == '3':
            money += 79
        elif text == '4':
            money += 109
        elif text == '5':
            money += 99
        elif text == '6':
            money += 49
        elif text == '7':
            money += 49
        elif text == '8':
            money += 59
        elif text == '9':
            money += 89
        elif text == '10':
            money += 69
        elif text == '11':
            money += 100
        elif text == '12':
            money += 150
        elif text == '13':
            money += 79
        elif text == '14':
            money += 53
        elif text == '15':
            money += 53
        else :
            update.message.reply_text("請輸入數字1~15")
            return False
        return True

    def is_going_to_state3(self, update):
        text = update.message.text
        return text == '甜心卡'

    def is_going_to_state6(self, update):
        text = update.message.text
        global money
        if text == '1':
            money +=40
        elif text == '2':
            money +=55
        elif text == '3':
            money +=43
        elif text == '4':
            money +=49
        elif text == '5':
            money +=69
        elif text == '6':
            money +=95
        elif text == '7':
            money +=52
        elif text == '8':
            money +=52
        else :
            update.message.reply_text("請輸入數字1~8")
            return False
        return True

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '1+1'

    def is_going_to_state7(self, update):
        text = update.message.text
        if text != '1' and text != '2' and text != '3' and text != '4' and text != '5' and text != '6' and text != '7' and text != '8' and text != '9' :
            update.message.reply_text("請輸入數字1~9")
            return False
        else :
            global money
            money += 50
            return True

    def is_going_to_state8(self, update):
        text = update.message.text
        global money
        if text == '1' or text == '2' or text == '3' or text == '4' or text == '5' or text == '6':
            money += 0
        elif text == 'A':
            money += 46
        elif text == 'B':
            money += 46
        elif text == 'C':
            money += 65
        elif text == 'D':
            money += 65
        elif text == 'E':
            money += 79
        elif text == 'F':
            money += 0
        else:
            update.message.reply_text("請輸入正確代號")
            return False
        update.message.reply_text("總金額是："+str(money))
        return True

    def go_back(self, update):
        text = update.message.text
        if text == '繼續點餐':
            return True
        elif text == '結帳':
            self.reset(update)
        else:
            update.message.reply_text("蛤 你說什麼？")
            return False

    def on_enter_state1(self, update):
        update.message.reply_text("歡迎光臨,請問需要什麼？\n>超值全餐\n>甜心卡\n>1+1")

    def on_enter_state2(self, update):
        chat_id = update.message.chat_id
        bot.send_photo(chat_id=chat_id, photo='https://twcoupon.com/images/menu/p_mcdonalds/lunch.jpg')
        update.message.reply_text("那請問需要幾號餐呢？\n\
        1. 大麥克----------------$69\n\
        2. 雙層牛肉吉事堡-------$59\n\
        3. 四盎司牛肉堡---------$79\n\
        4. 雙層四盎司牛肉堡-----$109\n\
        5. 1995美式培根牛肉堡--$99\n\
        6. 麥香魚----------------$49\n\
        7. 麥香雞----------------$49\n\
        8. 麥克雞塊（6塊）------$59\n\
        9. 麥克雞塊（9塊）------$89\n\
        10. 勁辣雞腿堡-----------$69\n\
        11. 麥脆雞（2塊）--------$100\n\
        12. 麥脆雞（3塊）-------$150\n\
        13. 板烤雞腿堡-----------$79\n\
        14. 黃金起司豬排堡-------$53\n\
        15. 大大雞腿堡-----------$53")

    def on_enter_state3(self, update):
        chat_id = update.message.chat_id
        bot.send_photo(chat_id=chat_id, photo='http://www.cardu.com.tw/image_upload/images/Cardu20170315_08512216.jpg')
        update.message.reply_text("買A\n\
        1. 大杯冰紅茶(檸檬風味)/冰綠茶(無糖)/汽水--$40\n\
        2. 冰旋風----------------------------------$55\n\
        3. 熱/冰美式咖啡/熱/冰焦糖奶茶-------------$43\n\
        4. 四塊麥克雞塊----------------------------$49\n\
        5. 六塊麥克雞塊----------------------------$69\n\
        6. 九塊麥克雞塊----------------------------$95\n\
        7. 大包薯條(上午10:30後供應)---------------$52\n\
        8. 大杯玉米濃湯----------------------------$52")

    def on_enter_state4(self, update):
        chat_id = update.message.chat_id
        bot.send_photo(chat_id=chat_id, photo='https://twcoupon.com/couponimage/231740_n.jpg')
        update.message.reply_text("請問要搭配什麼？\n1. 法式芥末香雞堡\n2. 美式辣味香雞堡\n3. 四塊麥克雞塊\n4. 小包薯條\n5. 鬆餅（兩片）\n6. BBQ嫩雞翅（一份兩塊）\n7. 勁辣香雞翅\n8. 聖代（芝麻/巧克力）\n9. 蘋果派")

    def on_enter_state5(self, update):
        update.message.reply_text("請問您的配餐選擇是？\n\
        A. 經典配餐（中薯+33$冷/熱飲）--------------$46\n\
        B. 清爽配餐（四季沙拉+33$冷/熱飲）----------$46\n\
        C. 酷炫配餐（冰旋風+33$冷/熱飲）------------$65\n\
        D. 勁脆配餐（麥脆雞+33$冷/熱飲）------------$65\n\
        E. 豪邁配餐（無骨雞腿排+小薯+33$冷/熱飲）--$79\n\
        F. 不要配餐")

    def on_enter_state6(self, update):
        update.message.reply_text("送B\n1. 大杯可口可樂/可口可樂zero/雪碧\n2. 大杯冰紅茶/冰綠茶\n3. 蛋捲冰淇淋\n4. 經典冰咖啡\n5. 小杯焦糖熱奶茶/熱紅茶\n6. 小杯經典美式咖啡/熱巧克力")

    def on_enter_state7(self, update):
        update.message.reply_text("1. 經典美式咖啡（小）/熱紅茶\n2. 小杯可樂/雪碧/冰綠茶/冰紅茶\n3. 小杯玉米濃湯")

    def on_enter_state8(self, update):
        update.message.reply_text("\n請問要繼續點餐還是結帳？\n>繼續點餐\n>結帳")



