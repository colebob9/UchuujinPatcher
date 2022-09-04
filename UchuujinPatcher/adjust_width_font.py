import struct

def adjust_width_font():
    font = open("work/isofiles/lt_patched.bin", "r+b")
    dic = {
    0x0000:4,#space
    0x0001:5,#、
    0x0002:4,#。
    0x0003:4,#，
    0x0004:4,#．
    0x0005:9,#・
    0x0006:9,#：
    0x0007:9,#；
    0x0008:9,#？
    0x0009:9,#！
    0x000A:4,#゛
    0x000B:4,#゜
    0x000C:2,#´
    0x000D:9,#｀
    0x000E:9,#¨
    0x000F:9,#＾
    0x0010:9,#￣
    0x0011:9,#＿
    0x0012:9,#ヽ
    0x0013:9,#ヾ
    0x0014:9,#ゝ
    0x0015:9,#ゞ
    0x0016:9,#〃
    0x0017:9,#仝
    0x0018:9,#々
    0x0019:9,#〆
    0x001A:9,#〇
    0x001B:9,#ー
    0x001C:9,#―
    0x001D:9,#‐
    0x001E:9,#／
    0x001F:9,#\
    0x0020:9,#〜
    0x0021:9,#‖
    0x0022:9,#｜
    0x0023:9,#…
    0x0024:9,#‥
    0x0025:9,#‘
    0x0026:9,#’
    0x0027:9,#“
    0x0028:9,#”
    0x0029:9,#（
    0x002A:9,#）
    0x002B:9,#〔
    0x002C:9,#〕
    0x002D:9,#［
    0x002E:9,#］
    0x002F:9,#｛
    0x0030:9,#｝
    0x0031:9,#〈
    0x0032:9,#〉
    0x0033:9,#《
    0x0034:9,#》
    0x0035:9,#「
    0x0036:9,#」
    0x0037:9,#『
    0x0038:9,#』
    0x0039:9,#【
    0x003A:9,#】
    0x003B:9,#＋
    0x003C:9,#−
    0x003D:9,#±
    0x003E:9,#×
    0x003F:9,#÷
    0x0040:9,#＝
    0x0041:9,#≠
    0x0042:9,#＜
    0x0043:9,#＞
    0x0044:9,#≦
    0x0045:9,#≧
    0x0046:9,#∞
    0x0047:9,#∴
    0x0048:9,#♂
    0x0049:9,#♀
    0x004A:9,#°
    0x004B:9,#′
    0x004C:9,#″
    0x004D:9,#℃
    0x004E:9,#￥
    0x004F:9,#＄
    0x0050:9,#¢
    0x0051:9,#£
    0x0052:9,#％
    0x0053:9,#＃
    0x0054:9,#＆
    0x0055:9,#＊
    0x0056:9,#＠
    0x0057:9,#§
    0x0058:9,#☆
    0x0059:9,#★
    0x005A:9,#○
    0x005B:9,#●
    0x005C:9,#◎
    0x005D:9,#◇
    0x005E:9,#◆
    0x005F:9,#□
    0x0060:9,#■
    0x0061:9,#△
    0x0062:9,#▲
    0x0063:9,#▽
    0x0064:9,#▼
    0x0065:9,#※
    0x0066:9,#〒
    0x0067:9,#→
    0x0068:9,#←
    0x0069:9,#↑
    0x006A:9,#↓
    0x006B:9,#〓
    0x006C:9,#∈
    0x006D:9,#∋
    0x006E:9,#⊆
    0x006F:9,#⊇
    0x0070:9,#⊂
    0x0071:9,#⊃
    0x0072:9,#∪
    0x0073:9,#∩
    0x0074:9,#∧
    0x0075:9,#∨
    0x0076:9,#¬
    0x0077:9,#⇒
    0x0078:9,#⇔
    0x0079:9,#∀
    0x007A:9,#∃
    0x007B:9,#∠
    0x007C:9,#⊥
    0x007D:9,#⌒
    0x007E:9,#∂
    0x007F:9,#∇
    0x0080:9,#≡
    0x0081:9,#≒
    0x0082:9,#≪
    0x0083:9,#≫
    0x0084:9,#√
    0x0085:9,#∽
    0x0086:9,#∝
    0x0087:9,#∵
    0x0088:9,#∫
    0x0089:9,#∬
    0x008A:9,#Å
    0x008B:9,#‰
    0x008C:9,#♯
    0x008D:9,#♭
    0x008E:9,#♪
    0x008F:9,#†
    0x0090:9,#‡
    0x0091:9,#¶
    0x0092:6,#0
    0x0093:3,#1
    0x0094:6,#2
    0x0095:6,#3
    0x0096:6,#4
    0x0097:5,#5
    0x0098:5,#6
    0x0099:6,#7
    0x009A:6,#8
    0x009B:5,#9
    0x009C:7,#Ａ
    0x009D:5,#Ｂ
    0x009E:6,#Ｃ
    0x009F:6,#Ｄ
    0x00A0:5,#Ｅ
    0x00A1:6,#Ｆ
    0x00A2:6,#Ｇ
    0x00A3:6,#Ｈ
    0x00A4:2,#Ｉ
    0x00A5:4,#Ｊ
    0x00A6:6,#Ｋ
    0x00A7:5,#Ｌ
    0x00A8:7,#Ｍ
    0x00A9:5,#Ｎ
    0x00AA:7,#Ｏ
    0x00AB:5,#Ｐ
    0x00AC:6,#Ｑ
    0x00AD:5,#Ｒ
    0x00AE:5,#Ｓ
    0x00AF:5,#Ｔ
    0x00B0:5,#Ｕ
    0x00B1:6,#Ｖ
    0x00B2:7,#Ｗ
    0x00B3:5,#Ｘ
    0x00B4:5,#Ｙ
    0x00B5:5,#Ｚ
    0x00B6:5,#ａ
    0x00B7:5,#ｂ
    0x00B8:5,#ｃ
    0x00B9:5,#ｄ
    0x00BA:5,#ｅ
    0x00BB:3,#ｆ
    0x00BC:5,#ｇ
    0x00BD:5,#ｈ
    0x00BE:2,#ｉ
    0x00BF:3,#ｊ
    0x00C0:4,#ｋ
    0x00C1:2,#ｌ
    0x00C2:7,#ｍ
    0x00C3:5,#ｎ
    0x00C4:5,#ｏ
    0x00C5:5,#ｐ
    0x00C6:5,#ｑ
    0x00C7:3,#ｒ
    0x00C8:5,#ｓ
    0x00C9:3,#ｔ
    0x00CA:5,#ｕ
    0x00CB:5,#ｖ
    0x00CC:7,#ｗ
    0x00CD:5,#ｘ
    0x00CE:5,#ｙ
    0x00CF:5,#ｚ
    }
    for i in range(3516):
        d = font.read(0x5b)
        try:
            w = dic[i]
            #print(i,":",w,",")
        except:
            w = 9
        font.write(struct.pack("B",w))


if __name__ == "__main__":
    adjust_width_font()
