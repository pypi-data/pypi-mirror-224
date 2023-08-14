#coding=utf-8
# 当前版本
current_version = 1.0
'''
版本号：V5.18 2023.06.30 朱永彬
学生版

版本号：V5.17 2023.06.15 朱永彬
1、添加了isGo()函数，判断前方是否有障碍物，有则True，没有则False。
2、当地图元素中没有停车场的时候，自动切换判断胜利的方式。
3、当导入Excel地图时，自动加载地图。

版本号：V5.14 2023.05.17 朱永彬
1、添加了导入Excel单个地图功能。
inputMap() /  mapInput()

版本号：V5.13 2023.05.11 朱永彬
1、添加了水果元素，在地图中用F表示。

版本号：V5.12 2023.04.05 朱永彬
1、优化了更新界面。
2、优化了更新算法。
3、将更新包移动到res/backup/中，不直接存放于根目录
4、单文件适配，只有turing.py文件也可以弹出更新窗口，通过联网下载依赖文件来运行整个程序。

版本号：V5.0 2023.04.01 蔡辉龙
C2使用
1、增加判断主角前方是否是陷阱，是返回1，否返回0，用于作为分支时的条件指令
1.1、主角增加行为属性：isTrap(self)
1.2、二次封装调用主角行为属性：isTrap()


版本号：V4.0 2023.03.22 朱永彬
1. 调整地图结构：每一张地图为一个字典，以列表嵌套字典的形式储存在res/map中。
2. 首次使用打开一键转为json即可转换。
3. map中的所有json文件都会合并使用。


版本号：V3.9 2023.03.16 蔡辉龙
1、删除：pickUp()函数中，与陷阱碰撞后，无需再创建空白地板
2、放置到目标位置
2.1、增加目标位置的图片素材：_TARGET_IMGS = ['目标点.jpg']，config.ini中，"2"表示目标点
2.2、增加目标点坐标的存放列表：_target_pos = []，_putdown_errpos ＝[]
2.3、修改_creatFloor()函数：global _target_pos，增加对目标图片2的判断与创建，并把目标点坐标以元组形式存放到_target_pos中
2.4、修改_clear()函数：global _target_pos，_putdown_pos，增加语句_target_pos = [] ，_putdown_errpos ＝[]
2.5、修改putDown()函数：global _target_pos，_putdown_errpos，当加入self.isOver()判断，是否放置正确，具体通关规则在isOver()函数中体现
2.6、就放置功能，复写isOver()函数
'''
'''
版本号：V3.8 2023.03.15 蔡辉龙
1、增加地图加载成功音效
1.1、变量：_sound_map = pygame.mixer.Sound(_PATH_SOUND+'加载.mp3')
1.2、loadMap()函数：global _sound_map；_sound_map.play()
2、增加：胜利、失败的图片和音效结果反馈
2.1、变量：_sound_win ,_sound_fial ,_image_win ,_image_fail
2.2、_showResult(flag=1)函数：实现结果图片与音效
2.3、在所有isOver()函数中，增加_showResu()函数的调用
'''
'''
版本号：V3.7 2023.03.14 蔡辉龙
1、屏蔽：二次封装的单步向前moveForward()
2、屏蔽：主角类中的turnLeftMoves()、turnRightMoves()、turnBackMoves()方法
3、修改：取消默认参数1
3.1、主角类中movesUp(self,n)、movesDown(self,n)、movesLeft(self,n)、movesRight(self,n)方法
3.2、二次封装movesUp(n)、movesDown(n)、movesLeft(n)、movesRight(n)方法
4、增加：撞击音效、遇险音效，sounds/撞击.wav、sounds/遇险.wav
4.1、初始化mixer，即pygame.mixer.init()
4.2、增加音效路径及音效常量：_PATH_SOUND = './res/sounds/' ,_sound_zj ,_sound_yx ,_sound_sq ,_sound_fz
#撞击声
_sound_zj = pygame.mixer.Sound(_PATH_SOUND+'撞击.mp3')
#遇险声
_sound_yx = pygame.mixer.Sound(_PATH_SOUND+'遇险.mp3')
#拾取声
_sound_sq = pygame.mixer.Sound(_PATH_SOUND+'拾取.mp3')
#放置声
_sound_fz = pygame.mixer.Sound(_PATH_SOUND+'放置.mp3')
4.3、修改isTop()、isEof()、isLeft()、isRight()：增加了global _sound_zj，_sound_zj.play()
4.4、修改pickUp()：对于宝物，global _sound_sq，_sound_sq.play()；对于陷阱，global _sound_yx，_sound_yx.play()
4.5、修改putDown()：
  global _sound_fz，_sound_fz.play()；
  重绘_drawAll()，self.draw()；
  条件修改，如果主角不在陷阱上，没有通关，且已收集到宝物、没有放置完，动作有效
5、增加_traps_pos = []，放于存放陷阱坐标
6、修改clear()：global _traps_pos，_traps_pos = []
7、修改_creatTrap()：global _traps_pos，_traps_pos.append( (traps.rect.left, traps.rect.top) )
'''
'''
版本号：V3.6 2023.03.13 蔡辉龙
1、屏蔽：turnBack()、turnLeftMoves()、turnRightMoves()、turnBackMoves()；让学生自己封装调用
2、增加单位扣血常量：_life_step，初始值为20
3、增加撞击数、遇险数变量：_zj = 0 ，_yx = 0
4、关联pickUp()修改：global _lie_step，_yx 和_life -= _life_step ，_yx += 1
5、修改：pickUp()，碰撞陷阱时，陷阱不消失，把碰撞参数改为False即可
6、修改：_drawAll()，调整绘制顺序，避免与陷阱碰撞后，地板绘制挡住了陷阱
7、修改：_changeTitle()，加增了撞击数、遇险数
8、修改：_clear()，global _zj,_yx，加增撞击数、遇险数的重置，_zj = 0 ，_yx = 0
9、修改：isEof()、isTop()、isLeft()、isRight()，补充global _zj、_zj += 1、调用_changeTitle()

'''
'''
版本号：V3.5 2023.03.13 朱永彬
1. 优化了地图配置工具

版本号：V3.4 2023.03.10 朱永彬
1. 添加了地图辅助功能
2. 修复了怪物碰撞问题

版本号：V3.2 2023.03.07 朱永彬
1.添加了自动更新的功能
2.由于字体文件太大，不加入更新列表队列。
3.当字体文件缺失时，自动使用系统默认字体。


版本号：V3.1
修改人：蔡辉龙
日期：2023年3月3号

增加项：
1、_changTitle()函数：把要显示的文本，作为窗体标题
2、通关规则集中增加：规则5的文字说明

删除项：
1、_writeText(title='')函数

修改项：
1、_loadFrom(title='')函数改为无参的_loadForm()函数
        删除：pygame.display.set_caption(f'Coding课程 {title.upper()}')
2、loadMap(title='')函数中，把调用的_loadFrom(title)改为调用_loadForm()
3、_drawAll()函数中
        增加：_changeTitle()函数的调用

待处理：放以后版本实现
1、游戏耗时计数
2、成功与失败
3、加音效、开关
4、遇险问答：对不扣血，反之扣血
'''

import pygame,os, random
import tkinter as tk
import tkinter.ttk as ttk
import urllib.request
import zipfile
import json
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, messagebox
import sys


# 更新检测
class Version_Control:
    def __init__(self):
        try:
            url = 'https://bbs.turingedu.cn/easycoding/version.json'
            r = urllib.request.urlopen(url,timeout=0.5)
            data = json.loads(r.read())
            latest_version = float(data.get("latest_version",'0'))
            url = data.get("download_url", '')
            if url and latest_version>current_version:
                filename = f'V{latest_version}.zip'
                tool = UpdateTool(url, filename)
                tool.run()
            else:
                print(f"O(∩_∩)O~")
        except:
            print(f"O(∩_∩)O~~")

# 更新操作
class UpdateTool:
    def __init__(self, url, filename):
        try:
            self.folder_path = "res/backup/"
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
            img = Image.open("res/images/messageBox.png")
            img = img.convert('RGBA')
            self.url = url
            self.filename = filename

            self.root = tk.Tk()
            self.root.overrideredirect(True)
            self.root.geometry("+250+250")
            self.root.lift()
            self.root.wm_attributes("-topmost", True)

            if sys.platform == 'win32':
                self.root.attributes('-transparentcolor', 'white')
            else:
                self.root.attributes('-transparent', True)

            self.offset_x = 0
            self.offset_y = 0
            self.root.bind("<ButtonPress-1>", self.start_drag)
            self.root.bind("<B1-Motion>", self.drag)
            self.photo = ImageTk.PhotoImage(img)

            self.label = Label(self.root, image=self.photo, bd=0, bg='white')
            self.label.pack()
            style = ttk.Style()
            style.theme_use('vista')  # clam/default/classic/vista 四种进度条风格
            self.update_button = Button(self.root, text="更新", command=self.start_update, bg="#3c6ddc", fg="#FFFFFF",
                                        font=("Helvetica", 12), padx=15, pady=5, activebackground="#0066CC")
            self.update_button.place(relx=0.3, rely=0.65)

            self.cancel_button = Button(self.root, text="取消", command=self.root.destroy, bg="#3c6ddc", fg="#FFFFFF",
                                        font=("Helvetica", 12), padx=15, pady=5, activebackground="#0066CC")
            self.cancel_button.place(relx=0.6, rely=0.65)

            self.root.attributes("-alpha", 1)
            self.update_button.configure(highlightthickness=0, foreground="#fee6da")
            self.cancel_button.configure(highlightthickness=0, foreground="#fee6da")
        except FileNotFoundError:
            self.url = url
            self.filename = filename
            self.root = tk.Tk()
            self.root.title('UpdateTool')
            self.root.geometry("350x130")
            self.root.wm_attributes("-topmost", 1)
            self.label = tk.Label(self.root, text="EasyCoding在线工具")
            self.label.pack(pady=10)
            self.update_button = tk.Button(self.root, text="更新", command=self.start_update_2)
            self.update_button.pack(side=tk.LEFT, padx=45)
            self.cancel_button = tk.Button(self.root, text="取消", command=self.root.destroy)
            self.cancel_button.pack(side=tk.RIGHT, padx=45)


    def start_drag(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def drag(self, event):
        x = self.root.winfo_x() + event.x - self.offset_x
        y = self.root.winfo_y() + event.y - self.offset_y
        self.root.geometry("+%s+%s" % (x, y))


    def run(self):
        self.root.mainloop()

    def start_update(self):
        self.progressbar = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
        self.progressbar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.progressbar.lower(self.update_button)
        self.download_zip()
        self.extract_zip()
        self.root.destroy()
        

    def start_update_2(self,type=1):
        self.progressbar = ttk.Progressbar(self.root, orient='horizontal', length=250, mode='determinate')
        self.progressbar.pack(pady=5)
        self.update_button.config(state=tk.DISABLED)
        self.download_zip()
        self.extract_zip()
        self.root.destroy()
        

    def download_zip(self):

        with urllib.request.urlopen(self.url) as response, open(self.folder_path+self.filename, 'wb') as out_file:
            content_length = int(response.headers.get('Content-Length'))
            chunk_size = 1024
            bytes_read = 0
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                bytes_read += len(chunk)
                percent = bytes_read / content_length * 100
                self.progressbar['value'] = percent
                self.root.update_idletasks()

    def support_gbk(self, zip_file: zipfile.ZipFile):
        name_to_info = zip_file.NameToInfo
        for name, info in name_to_info.copy().items():
            real_name = name.encode('cp437').decode('gbk')
            if real_name != name:
                info.filename = real_name
                del name_to_info[name]
                name_to_info[real_name] = info
        return zip_file

    def extract_zip(self):
        with self.support_gbk(zipfile.ZipFile(self.folder_path+self.filename)) as zfp:
            zfp.extractall(r'.')
        #messagebox.showinfo("更新", "更新成功。")
        quit()


Version_Control()





# 获胜方式【自动判断】
winType = 1
#窗体对象
_SCREEN = None
#窗体大小
_SCREEN_W ,_SCREEN_H = 800 ,600
#图片素材大小（主角、宝物、陷井、障碍物）
_IMG_W ,_IMG_H = 40,40
#地图
_thismap = ''
_mymap = ''
#图片路径
_PATH_IMG = './res/images/'
#背景图片名称
_BG_IMG = '5-_背景-800x600px.png'
#主角图片名称：4个方向的图片
_LEADER_IMGS = ['right.png','down.png','left.png','up.png']
#不可穿越的障碍物图片名称列表
_WALL1_IMGS = ['3-石头围挡.jpg']
_WALL2_IMGS = ['3-障碍-树.jpg','3-障碍-灌木.jpg']
_WALL3_IMGS = ['3-障碍-山.jpg','3-障碍-火山.jpg','3-障碍-沼泽.jpg']
#可拾取的宝物图片名称列表
_GEM_IMGS = ['2 -宝物-蓝钻石.jpg']
_GEM2_IMGS = ['1-宝物-西瓜.png','1-宝物-橙子.png','1-宝物-香蕉.png']
#陷井图片名称列表
_TRAPS_IMGS = ['1-陷阱-刺猬.jpg','1-陷阱-毒蛇.jpg','1-陷阱-狼.jpg','1-陷阱-老虎.jpg','1-陷阱-野猪.jpg']
#地板图片名称列表
_FLOOR_IMGS = ['4 -透明背景方框.jpg']
#目标点图片
_TARGET_IMGS = ['目标点.jpg']

#背景对象：存放背景图片各数据
_image_back = None
#障碍物组：根据地图初始化
_walls_sprite = pygame.sprite.Group()
#只存放所有障碍物坐标
_walls_pos = []
#宝物组：根据地图初始化
_gems_sprite = pygame.sprite.Group()
#陷井组：根据地图初始化
_traps_sprite = pygame.sprite.Group()
#只存放所有陷阱坐标
_traps_pos = []
#地板组：根据地图初始化
_floors_sprite = pygame.sprite.Group()
#只存放所有目标点坐标
_target_pos = []
#只存放放置错误位置的坐标
_putdown_errpos = []
#背包组：存放所收集的宝物，用于在地图上放置与重现
_saves_sprite = pygame.sprite.Group()
#背包列表：临时存放收集宝物，放置时转称到背包组
_saves = []
#主角对象
_leader = None
#刷新频率：毫秒
_FPS = 250

#生命值
_life = 100
#收集数量
_sc = 0
#计时
_mytime = 0
#总步数
_steps = 0
#单位扣血常量
_life_step = 20
#撞击数
_zj = 0
#遇险数
_yx = 0

#初始化mixer
pygame.mixer.init()
#声音路径
_PATH_SOUND = './res/sounds/'
#加载地图成功
_sound_map = pygame.mixer.Sound(_PATH_SOUND+'加载.mp3')
#撞击声
_sound_zj = pygame.mixer.Sound(_PATH_SOUND+'撞击.mp3')
#遇险声
_sound_yx = pygame.mixer.Sound(_PATH_SOUND+'遇险.mp3')
#拾取声
_sound_sq = pygame.mixer.Sound(_PATH_SOUND+'拾取.mp3')
#放置声
_sound_fz = pygame.mixer.Sound(_PATH_SOUND+'放置.mp3')

#胜利声
_sound_win = pygame.mixer.Sound(_PATH_SOUND+'胜利.mp3')
#失败声
_sound_fail = pygame.mixer.Sound(_PATH_SOUND+'失败.mp3')

#游戏结果
_image_win = pygame.image.load(_PATH_IMG+'胜利.png')
_image_win = pygame.transform.smoothscale(_image_win ,[320 ,180])
_image_fail = pygame.image.load(_PATH_IMG+'失败.png')
_image_fail = pygame.transform.smoothscale(_image_fail ,[320 ,180])


#字体
_PATH_FONT = './res/fonts/'
pygame.font.init()
try:
  _font = pygame.font.Font(_PATH_FONT+'msyh.ttc',22)
except:
  _font = pygame.font.Font(None,22)



#定义清除事件队列装饰器
def __clear__(f):
  def m(*args,**kwargs):
    x = f(*args, **kwargs)
    pygame.event.clear()
    return x
  return m

##精灵基类
class _MySprite(pygame.sprite.Sprite):
  #基类初始化：加载图片并获取图片信息
  def __init__(self,imagepath):
    try:
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface([_IMG_W ,_IMG_H])
      self.image = pygame.image.load(imagepath)
      self.image = pygame.transform.smoothscale(self.image ,[_IMG_W ,_IMG_H])
      self.rect = self.image.get_rect()
    except:
      print('图片加载错误，可能原因为图片文件夹路径或图片大小没有设定。')
  
  #绘制图片
  @__clear__
  def draw(self):
    _SCREEN.blit(self.image ,self.rect)
    pygame.display.flip()
    pygame.time.delay(_FPS)    

##单个物品子类
class _Object(_MySprite):
  #初始化
  def __init__(self,imgs=[]):
    try:
      super().__init__(_PATH_IMG+random.choice(imgs))
      self.rect.left = random.choice([0,40,80,120,160,200,240,280,320,360,400,440,480,520,560,600,640,680,720,760])
      self.rect.top = random.choice([0,40,80,120,160,200,240,280,320,360,400,440,480,520,560])
    except:
      print('imgs参数错误，必须是列表且元素不为空。')

##主角子类
class Leader(_MySprite):
  #主角初始化：创建并最初方向
  def __init__(self):    
    for i in range(len(_mymap)):
      for j in range(len(_mymap[i])):
        if _mymap[i][j].upper() in ['R','D','L','U']:
          if _mymap[i][j].upper() == 'R':
            self.arrow = _LEADER_IMGS[0]
          elif _mymap[i][j].upper() == 'D':
            self.arrow = _LEADER_IMGS[1]
          elif _mymap[i][j].upper() == 'L':
            self.arrow = _LEADER_IMGS[2]
          elif _mymap[i][j].upper() == 'U':
            self.arrow = _LEADER_IMGS[3]            
          super().__init__(_PATH_IMG+self.arrow)
          self.rect.left = j*_IMG_W
          self.rect.top = i*_IMG_H
          break

  #判断前方是否能走：能走1，不能走0
  def isGo(self):
    global _traps_pos
    global _walls_pos
    next_pos = ()
    #计算主角当前朝向前方的坐标
    if self.arrow == _LEADER_IMGS[0]:#右
      next_pos = (self.rect.left + _IMG_W, self.rect.top)
    elif self.arrow == _LEADER_IMGS[1]:#下
      next_pos = (self.rect.left, self.rect.top + _IMG_H)
    elif self.arrow == _LEADER_IMGS[2]:#左
      next_pos = (self.rect.left - _IMG_W, self.rect.top)
    elif self.arrow == _LEADER_IMGS[3]:#上
      next_pos = (self.rect.left, self.rect.top - _IMG_H)
    #判断前方坐标是否在陷阱坐标组内
    #print(next_pos,_traps_pos)
    if next_pos not in _traps_pos+_walls_pos:
      return 1
    else:
      return 0


  #判断前向是否陷阱：是返回1，否返回0
  def isTrap(self):
    global _traps_pos
    next_pos = ()
    #计算主角当前朝向前方的坐标
    if self.arrow == _LEADER_IMGS[0]:#右
      next_pos = (self.rect.left + _IMG_W, self.rect.top)
    elif self.arrow == _LEADER_IMGS[1]:#下
      next_pos = (self.rect.left, self.rect.top + _IMG_H)
    elif self.arrow == _LEADER_IMGS[2]:#左
      next_pos = (self.rect.left - _IMG_W, self.rect.top)
    elif self.arrow == _LEADER_IMGS[3]:#上
      next_pos = (self.rect.left, self.rect.top - _IMG_H)
    #判断前方坐标是否在陷阱坐标组内
    print(next_pos,_traps_pos)
    if next_pos in _traps_pos:
      return 1
    else:
      return 0

  #判断是否到顶
  def isTop(self):
    global _zj ,_sound_zj
    flag = False
    if self.rect.top <= 0 or (self.rect.left, self.rect.top - _IMG_H) in _walls_pos:
      _zj += 1
      _sound_zj.play()
      _changeTitle()
      flag =True
    return flag

  #判断是否最左
  def isLeft(self):
    global _zj ,_sound_zj
    flag = False
    if self.rect.left <= 0 or (self.rect.left - _IMG_W, self.rect.top) in _walls_pos:
      _zj += 1
      _sound_zj.play()
      _changeTitle()
      flag =True
    return flag

  #判断是否到底
  def isEof(self):
    global _zj ,_sound_zj
    flag = False
    if self.rect.top >= _SCREEN_H - _IMG_H or (self.rect.left, self.rect.top + _IMG_H) in _walls_pos:
      _zj += 1
      _sound_zj.play()
      _changeTitle()
      flag =True
    return flag

  #判断是否最右
  def isRight(self):
    global _zj ,_sound_zj
    flag = False
    if self.rect.left >= _SCREEN_W - _IMG_W or (self.rect.left + _IMG_W, self.rect.top) in _walls_pos:
      _zj += 1
      _sound_zj.play()
      _changeTitle()
      flag =True
    return flag

##'''==================以下通关规则集=================='''

##  #规则1：不计伤害，集齐宝物即通关
##  def isOver(self):
##    if len(_gems_sprite)==0:
##      _showResult(1)
##      return 1
##    else:
##      return 0





  def isOver(self):
     global _life
     if winType==1:
       # 规则2：计算伤害，生命不为0且集齐宝物即通关
       global _life
       if _life == 0:
         _showResult(0)
         return -1
       elif len(_gems_sprite)==0:
         _showResult(1)
         return 1
       else:
         return 0
     elif winType==2:
        #规则4：计算伤害，集齐宝物且放置成功即通关
       if len(_putdown_errpos) != 0 or _life==0:
          _showResult(0)
          return -1
       elif len(_gems_sprite)==0 and len(_saves)==0 and len(_target_pos)==0:
          _showResult(1)
          return 1
       else:
          return 0

##  #规则3：计算伤害，生命满值且集齐宝物即通关
##  def isOver(self):
##    global _life
##    if _life < 100:
##      _showResult(0)
##      return -1
##    elif len(_gems_sprite)==0:
##      _showResult(1)
##      return 1
##    else:
##      return 0

##  

##'''==================以上通关规则集=================='''
  
  #单步上移
  def moveUp(self):
    if self.isOver() != 0 or self.isTop():
      return -1
    global _steps
    self.rect.top -= _IMG_H
    _steps += 1
    self.pickUp()
    _drawAll()
    self.draw()
    self.isOver()

  #单步下移
  def moveDown(self):
    if self.isOver() != 0 or self.isEof():
      return -1
    global _steps
    self.rect.top += _IMG_H
    _steps += 1
    self.pickUp()
    _drawAll()
    self.draw()
    self.isOver()

  #单步左移
  def moveLeft(self):
    if self.isOver() != 0 or self.isLeft():
      return -1
    global _steps
    self.rect.left -= _IMG_W
    _steps += 1
    self.pickUp()
    _drawAll()
    self.draw()
    self.isOver()

  #单步右移
  def moveRight(self):
    if self.isOver() != 0 or self.isRight():
      return -1
    global _steps
    self.rect.left += _IMG_W
    _steps += 1
    self.pickUp()
    _drawAll()
    self.draw()
    self.isOver()

  #多步上移
  def movesUp(self,n):
    try:
      for i in range(n):
        if self.isOver() != 0 or self.moveUp() == -1:
          break
    except:
      print('参数错误，必须是不小于0的整数。')

  #多步下移
  def movesDown(self,n):
    try:
      for i in range(n):
        if self.isOver() != 0 or self.moveDown() == -1:
          break
    except:
      print('参数错误，必须是不小于0的整数。')        

  #多步左移
  def movesLeft(self,n):
    try:
      for i in range(n):
        if self.isOver() != 0 or self.moveLeft() == -1:
          break
    except:
      print('参数错误，必须是不小于0的整数。')        

  #多步右移
  def movesRight(self,n):
    for i in range(n):
      if self.isOver() != 0 or self.moveRight() == -1:
        break

  #加载图片：转向时调用
  def imageLoad(self):
    self.image = pygame.image.load(_PATH_IMG+self.arrow)
    self.image = pygame.transform.smoothscale(self.image ,[_IMG_W ,_IMG_H])
    
  #当前方向左转
  def turnLeft(self):
    if self.isOver() != 0:
      return -1
    global _steps
    if self.arrow == _LEADER_IMGS[1]:
      self.arrow = _LEADER_IMGS[0]
    elif self.arrow == _LEADER_IMGS[0]:
      self.arrow = _LEADER_IMGS[3]
    elif self.arrow == _LEADER_IMGS[3]:
      self.arrow = _LEADER_IMGS[2]
    else:
      self.arrow = _LEADER_IMGS[1]
    self.imageLoad()
    _steps += 1
    _drawAll()
    self.draw()

  #当前方向右转
  def turnRight(self):
    if self.isOver() != 0:
      return -1
    global _steps
    if self.arrow == _LEADER_IMGS[1]:
      self.arrow = _LEADER_IMGS[2]
    elif self.arrow == _LEADER_IMGS[2]:
      self.arrow = _LEADER_IMGS[3]
    elif self.arrow == _LEADER_IMGS[3]:
      self.arrow = _LEADER_IMGS[0]
    else:
      self.arrow = _LEADER_IMGS[1]
    self.imageLoad()
    _steps += 1
    _drawAll()
    self.draw()

  #当前方向后转
  def turnBack(self):
    if self.isOver() != 0:
      return -1
    global _steps
    if self.arrow == _LEADER_IMGS[1]:
      self.arrow = _LEADER_IMGS[3]
    elif self.arrow == _LEADER_IMGS[3]:
      self.arrow = _LEADER_IMGS[1]
    elif self.arrow == _LEADER_IMGS[0]:
      self.arrow = _LEADER_IMGS[2]
    else:
      self.arrow = _LEADER_IMGS[0]
    self.imageLoad()
    _steps += 1
    _drawAll()
    self.draw()

  #当前方向向前移动一步
  def moveForward(self):
    if self.isOver() != 0:
      return -1
    global _steps
    if self.arrow == _LEADER_IMGS[0] and not self.isRight():
      self.rect.left += _IMG_W
    elif self.arrow == _LEADER_IMGS[1] and not self.isEof():
      self.rect.top += _IMG_H
    elif self.arrow == _LEADER_IMGS[2] and not self.isLeft():
      self.rect.left -= _IMG_W
    elif self.arrow == _LEADER_IMGS[3] and not self.isTop():
      self.rect.top -= _IMG_H
    else:
      return -1
    _steps += 1
    self.pickUp()
    _drawAll()
    self.draw()
    self.isOver()

  #当前方向向前多步移动
  def movesForward(self,n=1):
    try:
      for i in range(n):
        if self.isOver() != 0 or self.moveForward() == -1:
          break
    except:
      print('参数错误，必须是不小于0的整数。')        

##  #当前方向左转后多步移动
##  def turnLeftMoves(self,n=1):
##    self.turnLeft()
##    self.movesForward(n)
##
##  #当前方向右转后多步移动
##  def turnRightMoves(self,n=1):
##    self.turnRight()
##    self.movesForward(n)
##
##  #当前方向后转后多步移动
##  def turnBackMoves(self,n=1):
##    self.turnBack()
##    self.movesForward(n)
  
  #碰撞：拾起宝物
  def pickUp(self):
    _get_sprite = pygame.sprite.spritecollide(self, _gems_sprite, True)
    if _get_sprite:
      global _sc, _sound_sq
      _sc += 1
      if len(_get_sprite):
        _saves.append(_get_sprite[0])
        FLOOR = _Object(_FLOOR_IMGS)
        FLOOR.rect.left = self.rect.left
        FLOOR.rect.top = self.rect.top
        _floors_sprite.add(FLOOR)
        _sound_sq.play()
    elif pygame.sprite.spritecollide(self, _traps_sprite, False):
      global _life ,_life_step ,_yx   
      _life -= _life_step
      _yx += 1
      _sound_yx.play()

  #放置物品：绘制要放置的物品，不能放置到陷井上
  def putDown(self):
    global _sound_fz ,_traps_pos ,_putdown_errpos
    if ((self.rect.left, self.rect.top) not in _traps_pos) and self.isOver() == 0 and len(_saves)>0:
      _saves[0].rect.x = self.rect.x
      _saves[0].rect.y = self.rect.y
      _saves_sprite.add(_saves.pop(0))
      _sound_fz.play()
      _drawAll()
      self.draw()
      if ((self.rect.left, self.rect.top) not in _target_pos):
        _putdown_errpos.append((self.rect.left, self.rect.top))
      else:
        _target_pos.remove((self.rect.left, self.rect.top))
      self.isOver()

# 居中地图
def align_map(map):
    h = len(map)
    w = len(map[0])
    aligned_map = [['0' for _ in range(20)] for _ in range(15)]
    for i in range(h):
        for j in range(w):
            if i >= 15 or j >= 20:
                break
            aligned_map[7+i-h//2][10+j-w//2] = map[i][j]
    return aligned_map

#生成随机地图
def gen_map(width, height, difficulty):
    # difficulty = difficulty//10
    # 当难度为0时，防止被除数为0，设置为-1，无难度。
    # 当难度小于1时不为0时，设置最小难度值，为1。
    difficulty = difficulty if difficulty>1 else -1 if difficulty==0 else 1
    # 生成空地图
    map = [['1' for _ in range(width)] for _ in range(height)]
    # 生成边界
    for i in range(height):
        map[i][0] = '#'
        map[i][width-1] = '#'
    for i in range(width):
        map[0][i] = '#'
        map[height-1][i] = '#'
    # 生成人物
    x = 0
    y = 0
    while map[x][y] != '1':
        x = random.randint(1, height-2)
        y = random.randint(1, width-2)
    map[x][y] = 'D'

    # 怪兽、宝石、障碍物的数量
    obstacle_num = int((width * height * difficulty) / 300)
    gem_num = int((width * height * difficulty) / 200)
    monster_num = int((width * height * difficulty) / 300)
    all_num = obstacle_num+gem_num+monster_num

    # 当放置物品的数量超过地图区域的80%时，重新生成。并且难度-1。
    if sum(map,[]).count('1')*0.8<all_num:
        return gen_map(width, height, difficulty - 1)
    # 当怪兽、宝石、障碍物其中有一个为0时，让难度+1，这样不会导致没有放置物。
    elif obstacle_num*gem_num*monster_num==0:
        return gen_map(width, height, difficulty + 1)

    # 障碍物（T/N/X）
    obstacle_types = ['T', 'N', 'X']
    obstacle_count = 0

    while obstacle_count < obstacle_num:
        x = random.randint(1, height-2)
        y = random.randint(1, width-2)
        if map[x][y] == '1':
            map[x][y] = obstacle_types[random.randint(0, 2)]
            obstacle_count += 1

    # 宝石（$）
    gem_count = 0
    while gem_count < gem_num:
        x = random.randint(1, height-2)
        y = random.randint(1, width-2)
        if map[x][y] == '1':
            map[x][y] = '$'
            gem_count += 1

    # 怪兽(X)
    monster_count = 0
    while monster_count < monster_num:
        x = random.randint(1, height-2)
        y = random.randint(1, width-2)
        if map[x][y] == '1':
            map[x][y] = 'X'
            monster_count += 1

    return align_map(map)


# 打印地图
def print_map(map):
    print("config版本".center(40,"#"))
    print("C1LX_XX = [")
    for row in range(len(map)):
        s = f'''\t\t{str(map[row]).replace("'",'"').replace(" ","")},'''
        print(s if row!=len(map)-1 else s.strip(","))
    print("\t]")

    print("Excel版本".center(40,"#"))
    for row in map:
        print("\t".join(row))

    # for row in map:
    #     print(" ".join(row))


def mapInput():
    def output(map,title=None):
        if title==None:
            title=f"C1LX_{int(random.random()*100)}"

        text = []
        text.append("[")
        for row in range(len(map)):
            s = f'''\t\t{str(map[row]).replace("'", '"').replace(" ", "")},'''
            text.append(s if row != len(map) - 1 else s.strip(","))
        text.append("\t]")
        text = "\n".join(text)

        item = {
            "title": title,
            "map": json.loads(text)
        }

        t = title.split("_")
        file_name = t[0] if len(t)==2 and not t[0].endswith("X") else "自定义地图"
        try:
            # 以字符串形式读取json文件内容
            map_json = json.load(open(f'res/map/{file_name}.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            map_json = []

        # text = open(f'res/map/{file_name}.json', 'r', encoding='utf-8').read()
        for i,map in enumerate(map_json):
            if title == map["title"]:
                while True:
                    n = input(f"【{title}】当前地图已存在，请选择操作方式：\n[1]覆盖\n[2]追加(保留新旧)\n[3]取消\n\n请选择：")
                    if n=="1":
                        map_json[i] = item
                        break
                    elif n=="2":
                        map_json.append(item)
                        break
                    elif n=="3":
                        print("操作已取消")
                        return 0
                break
        else:
            map_json.append(item)
        text = json.dumps(map_json,indent=4,ensure_ascii=False).replace('''",
                "''','","').replace('''[
                "''','["').replace('''"
            ]''','"]')
        # 重新导出替换后的json文件
        # print(text)
        with open(f'res/map/{file_name}.json', 'w', encoding='utf-8') as f:
            f.write(text.replace("],\n\t\t]", "]\n\t\t]"))
        print(f"地图【{title}】已成功导入到res/map/{file_name}.json")
        # n = input("是否加载该地图（Y/N）：")
        # if n.lower()!="n":
        loadMap(title)


    Excel版地图=[]
    while True:
        sc = input()
        if sc:
            Excel版地图.append(sc)
        else:
            break
    Excel版地图 = "\n".join(Excel版地图)
    li = Excel版地图.strip().split("\n")
    if len(li) == 17:
        map = [[j if j else '0' for j in i.split("\t")[1:]] for i in li[2:]]
        output(map, li[0].strip())
    elif len(li) == 15:
        map = [[j if j else '0' for j in i.split("\t")] for i in li]
        output(map)
    else:
        print("格式有误")

inputMap =mapInput
'''
二次封装
'''
##加载：窗体、背景、地图（障碍物、宝物）、主角
def loadMap(title=None):
  global _mymap, _thismap,_sound_map,isOver
  # import configparser, json
  try:
    if title and type(title)==str:
        # 获取map文件夹的所有json文件
        json_files = [f for f in os.listdir("res/map") if f.endswith('.json')]
        # print(json_files)
        # 合并json文件
        items = {}
        file = ""
        for file in json_files:
            with open(f"res/map/{file}", "r",encoding="utf-8") as f:
                data = json.load(f)
                # print(data)
                for i in data:
                  i['title'] = i['title'].upper()
                  items[i['title']] = i

        # config = configparser.ConfigParser(allow_no_value=True)
        # config.read('config.ini')
        _thismap = title.upper()
        # print(items)
        if _thismap in items:
            _mymap = items[_thismap].get("map",[])

        else:
            raise Exception(f"{_thismap}该地图不存在")
        # _mymap = config.get('map',_thismap)
        # _mymap = json.loads(_mymap)
        # _mymap = align_map(_mymap)
        # print(_mymap)
    else:
        if type(title)==list and len(title)>=3:
            _mymap = gen_map(title[0], title[1], title[2])
            if len(title)>=4 and title[3]==True:
                print_map(_mymap)
        elif type(title)==int:
            _mymap = gen_map(20, 15, title)
        else:
            # 当不传值时触发
            # _mymap = gen_map(20, 15, random.randint(10,50))
            raise Exception("请传入地图")

  except json.decoder.JSONDecodeError:
      print(f'【{file}】文件格式有误')
  except:
      print(f'【{title}】该地图配置有误')
  else:
    _clear()
    _loadForm()
    _loadBg()
    _creatWall()
    _creatFloor()
    _creatGem()
    _creatTrap()
    _drawAll()
    _creatLeader()

    try:
        _leader.draw()
        _sound_map.play()
    except:
        print(f'主角错误，请检查config.ini文件中map项下{title.upper()}中是否有主角，分别用D、U、L、R表示。')

##加载：窗体
def _loadForm():
  global _SCREEN, _SCREEN_W ,_SCREEN_H  
  os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0,30)
  pygame.init()  
  _SCREEN = pygame.display.set_mode([_SCREEN_W ,_SCREEN_H] ,0 ,32)

##加载：背景
def _loadBg():
  global _SCREEN, _image_back, PATH_IMG, _BG_IMG, _SCREEN_W ,_SCREEN_H
  _image_back = pygame.image.load(_PATH_IMG+_BG_IMG).convert_alpha()
  _image_back = pygame.transform.smoothscale(_image_back ,[_SCREEN_W ,_SCREEN_H])
  _SCREEN.blit(_image_back ,(0 ,0))
  pygame.display.flip()

#清空初始化
def _clear():
  global   _SCREEN, _image_back, _thismap, _walls_sprite, _walls_pos, _gems_sprite, _traps_sprite, _traps_pos ,_floors_sprite,_saves_sprite, _saves, _leader, _life, _sc, _mytime, _steps,_zj,_yx ,_target_pos ,_putdown_errpos
  _SCREEN = None
  _image_back = None
  _walls_sprite = pygame.sprite.Group()
  _walls_pos = []
  _traps_pos = []
  _target_pos = []
  _putdown_errpos = []
  _gems_sprite = pygame.sprite.Group()
  _traps_sprite = pygame.sprite.Group()
  _floors_sprite = pygame.sprite.Group()
  _saves_sprite = pygame.sprite.Group()
  _saves = []
  _leader = None
  _life = 100
  _sc = 0
  _mytime = 0
  _steps = 0
  _zj = 0
  _yx = 0

#  
def restart():
  _clear()
  loadMap(_thismap)

##创建：障碍物
def _creatWall():
  global _walls_sprite, _walls_pos, _WALL_IMGS, _IMG_W, _IMG_H, _mymap,__walls_sprite_back
  for i in range(len(_mymap)):
    for j in range(len(_mymap[i])):
      if _mymap[i][j] == '#':
        wall = _Object(_WALL1_IMGS)
        wall.rect.left = j*_IMG_W
        wall.rect.top = i*_IMG_H
        _walls_sprite.add(wall)
        _walls_pos.append( (wall.rect.left, wall.rect.top) )
      elif _mymap[i][j].upper() == 'T':
        wall = _Object(_WALL2_IMGS)
        wall.rect.left = j*_IMG_W
        wall.rect.top = i*_IMG_H
        _walls_sprite.add(wall)
        _walls_pos.append( (wall.rect.left, wall.rect.top) )        
      elif _mymap[i][j].upper() == 'N':
        wall = _Object(_WALL3_IMGS)
        wall.rect.left = j*_IMG_W
        wall.rect.top = i*_IMG_H
        _walls_sprite.add(wall)
        _walls_pos.append( (wall.rect.left, wall.rect.top) )

##创建：宝物
def _creatGem():
  global _gems_sprite, _GEM_IMGS, _IMG_W, _IMG_H, _mymap
  for i in range(len(_mymap)):
    for j in range(len(_mymap[i])):
      if _mymap[i][j] == '$':
        gem = _Object(_GEM_IMGS)
        gem.rect.left = j*_IMG_W
        gem.rect.top = i*_IMG_H
        _gems_sprite.add(gem)      
      elif _mymap[i][j] == 'F':
        gem = _Object(_GEM2_IMGS)
        gem.rect.left = j*_IMG_W
        gem.rect.top = i*_IMG_H
        _gems_sprite.add(gem)

##创建：陷井
def _creatTrap():
  global _traps_sprite, _traps_pos ,_TRAPS_IMGS, _IMG_W, _IMG_H, _mymap
  for i in range(len(_mymap)):
    for j in range(len(_mymap[i])):
      if _mymap[i][j].upper() == 'X':
        traps = _Object(_TRAPS_IMGS)
        traps.rect.left = j*_IMG_W
        traps.rect.top = i*_IMG_H
        _traps_sprite.add(traps)
        _traps_pos.append( (traps.rect.left, traps.rect.top) )

##创建：地板
def _creatFloor():
  global winType,_floors_sprite, _FLOOR_IMGS, _IMG_W, _IMG_H, _mymap ,_TARGET_IMGS ,_target_pos
  for i in range(len(_mymap)):
    for j in range(len(_mymap[i])):
      if _mymap[i][j].upper() in ['1','F','U','D','L','R']:
        floors = _Object(_FLOOR_IMGS)
        floors.rect.left = j*_IMG_W
        floors.rect.top = i*_IMG_H
        _floors_sprite.add(floors)
      elif _mymap[i][j].upper() =='2':
        winType = 2
        floors = _Object(_TARGET_IMGS)
        floors.rect.left = j*_IMG_W
        floors.rect.top = i*_IMG_H
        _floors_sprite.add(floors)
        _target_pos.append( (floors.rect.left, floors.rect.top) )

#
def _changeTitle():
  _mytime = pygame.time.get_ticks()//1000
  pygame.display.set_caption(f'EasyCodingⅠ {_thismap}   【步数:{_steps}   耗时:{_mytime}s   集宝:{_sc}   撞击:{_zj}   遇险:{_yx}   生命:{_life}】')
  
##刷新重绘所有元素
def _drawAll():
  global _SCREEN,_image_back, _PATH_IMG, _BG_IMG, _SCREEN_W ,_SCREEN_H, _gems_sprite, _traps_sprite, _saves_sprite
  _image_back = pygame.image.load(_PATH_IMG+_BG_IMG).convert_alpha()
  _image_back = pygame.transform.smoothscale(_image_back ,[_SCREEN_W ,_SCREEN_H])
  _SCREEN.blit(_image_back ,(0 ,0))
  if len(_walls_sprite)>0:
    _walls_sprite.update()
    _walls_sprite.draw(_SCREEN)
  if len(_floors_sprite) > 0:
    _floors_sprite.update()
    _floors_sprite.draw(_SCREEN)    
  if len(_gems_sprite)>0:
    _gems_sprite.update()
    _gems_sprite.draw(_SCREEN)
  if len(_traps_sprite)>0:
    _traps_sprite.update()
    _traps_sprite.draw(_SCREEN)
  if len(_saves_sprite)>0:
    _saves_sprite.update()
    _saves_sprite.draw(_SCREEN)
  _changeTitle()
  pygame.display.flip()

#展示结果图片
def _showResult(flag=1):
  global _image_win ,_image_fail ,_sound_win ,_sound_fail
  if flag:
    _SCREEN.blit(_image_win ,((_SCREEN_W-320)/2 ,(_SCREEN_H-180)/2))
    _sound_win.play()
  else:
    _SCREEN.blit(_image_fail ,((_SCREEN_W-320)/2 ,(_SCREEN_H-180)/2))
    _sound_fail.play()
  pygame.display.flip()
  
##创建：主角
def _creatLeader():
  global _leader
  _leader = Leader()

#方向不变，上移一步
def moveUp():
  global _leader
  _leader.moveUp()

#方向不变，上移多步
def movesUp(n):
  global _leader
  _leader.movesUp(n)

#方向不变，下移一步
def moveDown():
  global _leader
  _leader.moveDown()

#方向不变，下移多步
def movesDown(n):
  global _leader
  _leader.movesDown(n)  

#方向不变，左移一步
def moveLeft():
  global _leader
  _leader.moveLeft()

#方向不变，左移多步
def movesLeft(n):
  global _leader
  _leader.movesLeft(n)  

#方向不变，右移一步
def moveRight():
  global _leader
  _leader.moveRight()

#方向不变，右移多步
def movesRight(n):
  global _leader
  _leader.movesRight(n)   

##原地左转
def turnLeft():
  global _leader
  _leader.turnLeft()

##原地右转
def turnRight():
  global _leader
  _leader.turnRight()

####原地后转
##def turnBack():
##  global _leader
##  _leader.turnBack()

####当前方向向前移动一步
##def moveForward():
##  global _leader
##  _leader.moveForward()
  
##当前方向向前移动多步，默认前移一步
def movesForward(step=1):
  global _leader
  _leader.movesForward(step)

####当前方向左转后移动多步
##def turnLeftMoves(step=1):
##  global _leader
##  _leader.turnLeftMoves(step)

####当前方向右转后移动多步
##def turnRightMoves(step=1):
##  global _leader
##  _leader.turnRightMoves(step)

####当前方向后转后移动多步
##def turnBackMoves(step=1):
##  global _leader
##  _leader.turnBackMoves(step)

#放置
def putDown():
  global _leader
  _leader.putDown()

#退出
def exit():
  pygame.quit()

#判断前方是否能走
def isGo():
  global _leader
  return _leader.isGo()

#判断前方是否陷阱
def isTrap():
  global _leader
  return _leader.isTrap()

















