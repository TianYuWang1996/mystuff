from sys import exit
from random import randint


class Scene(object):
    
    def enter(self):
        print("This scene is not yet configured. "
            "Subclass it and implement enter().")
        exit(1)

class Character(object):
    
    def __init__(self):
        self.HP = 10
        self.shoot_damage = 1
        self.dodge_percent = randint(0,10)/10

class Hero(Character):
    
    def __init__(self):
        self.HP = 10
        self.shoot_damage = 1
        self.dodge_percent = randint(0,10)/10

class Gothon(Character):
    
    def __init__(self):
        self.HP = 20
        self.shoot_damage = 2
        self.dodge_percent = randint(0,10)/10

class Fight(object):
    
    def __init__(self, fight1, fight2):
        self.fight1 = fight1
        self.fight2 = fight2
    
    def fight(self):
        while self.fight1.HP != 0 and self.fight2.HP != 0:

            self.fight2.HP = self.fight2.HP - self.fight1.shoot_damage * self.fight2.dodge_percent
            print("你向哥顿人开火，哥顿人剩余生命值为：%s" %self.fight2.HP)
            if self.fight2.HP == 0:
                print("你快速拔出枪并朝哥顿人开火。")
                print("你的激光枪击中了他的服装，让他整个燃烧起来。")
                print("趁他灭火时，你爆了他的头。")
                print("你穿过了武器库的门。")
                return "laser_weapon_armory"
                exit(0)
                
            self.fight1.HP = self.fight1.HP - self.fight2.shoot_damage * self.fight1.dodge_percent
            print("哥顿人向你开火。你的剩余生命值为：%s" %self.fight1.HP)
            if self.fight1.HP == 0:
                print("你快速拔出枪并朝哥顿人开火。")
                print("他灵活的移动让你失去了目标。")
                print("你的激光枪擦伤了他。")
                print("这让他非常愤怒，一枪将你爆头。")
                print("直到你死了，然后他吃了你。")
                return "death"
                exit(0)
            

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    
    quips = [
            "你死了。你在这有点糟糕",
            "干得漂亮，你死了，愚蠢的人类",
            "失败者",
            "我有只小狗很擅长这个"
    ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Central_Corridor(Scene):
    
    def enter(self):
        print("来自Percal25号行星的哥顿人入侵并破坏了你的飞船。")
        print("你的全体船员已经阵亡，你是最后的幸存者。")
        print("你的任务是从武器库中拿到中子自毁炸弹。")
        print("把它放在舰桥上，在你进入一个逃生仓后炸毁飞船。")
        print("\n")
        print("你正奔跑在中央走廊到武器库的路上。")
        print("这时一个哥顿人跳出来，红皮肤，黑牙齿，邪恶的服装。")
        print("怨恨充斥着他的身体，他正在挡在武器库的门外，好像正准备扔出炸弹炸死你。")
        
        Hero_1 = Hero()
        Gothon_1 = Gothon()
        
        action = input("> ")
    
        if action == "fight":
            Fight_1 = Fight(Hero_1, Gothon_1)
            return Fight_1.fight()
            
            
        elif action == "tell a joke":
            print("哥顿人喜欢听笑话。")
            print("你给他讲了个非常搞笑的笑话。")
            print("趁他不注意，你爆了他的头。")
            print("你穿过了武器库的门。")
        
            return "laser_weapon_armory"
        
        else:
            print("别想了!")
        
            return "central_corridor"


class Laser_Weapon_Armory(Scene):
    
    def enter(self):
        print("你打了个洞进入武器库。")
        print("这里死静死静的，好像埋伏着好多哥顿人。")
        print("你发现了中子炸弹，但是它被密码锁锁着。")
        print("你需要代码才能打开。")
        print("如果输错10次，密码锁将永远锁着。")
        print("提示：代码是3个数字。")
        
        code = ("%d%d%d" %(randint(1, 9), randint(1, 9), randint(1, 9)))
        guess = input("[keypad]> ")
        guesses = 1
        
        while guess != code and guesses < 10 and guess != "666666":
            print("BZZZZDDD!")
            guesses += 1
            guess = input("[keypad]> ")
        
        if guess == code or guess == "666666":
            print("锁打开了，飘荡出白色的气体。")
            print("你带着中子弹跑得越来越快。")
            print("你必须把中子弹放在舰桥正确的位置。")
            
            return "the_bridge"
            
        else:
            print("你最后一次听到了滴滴声。")
            print("锁永久锁定了。")
            print("你决定静静的坐着，最终哥顿人炸掉了飞船，你挂了。")
            
            return "death"


class The_Bridge(Scene):
    
    def enter(self):
        print("你带着中子弹突然出现在舰桥，惊动了5个哥顿人。")
        print("他们正试图控制飞船，他们每个人都穿着一套丑陋的服装。")
        print("他们还没有拿出武器。")
        print("他们看到你手上正拿着一个已经启动的炸弹。")
        print("他们不想看着它爆炸。")
        
        action = input("> ")
        
        if action == "throw the bomb":
            print("恐慌中，你把炸弹扔向了哥顿人。")
            print("这时一个哥顿人从背后把你射杀。")
            print("你倒地的时候看见一个哥顿人正在解除炸弹。")
            
            return "death"
            
        elif action == "slowly place the bomb":
            print("你指着手中的炸弹，哥顿人被吓到了，举起手来。")
            print("你慢慢地移动到门口，小心的把炸弹放到地上。")
            print("你把门锁住，哥顿人出不来。炸弹放置好了，你跑向逃生仓")
            print("炸弹放置好了，你跑向逃生仓。")
            
            return "escape_pod"
            
        else:
            print("别想了!")
            
        return "the_bridge"


class Escape_Pod(Scene):
    
    def enter(self):
        print("你冲向逃生仓，争取整个船爆炸前。")
        print("似乎船上没有其他哥顿人，你一路很顺利。")
        print("你来到逃生仓，这里有5个仓位。")
        print("你选择哪一个？")
        print("提示：序号1-5。")
        
        good_pod = randint(1, 5)
        guess = input("[pod #]> ")
        
        if int(guess) != good_pod and int(guess) != 666666:
            print("你跳进 %s 号逃生仓，按下了弹出按钮" %guess)
            print("逃生仓发生了爆炸，你挂了。")
            
            return "death"
            
        else:
            print("你跳进 %s 号逃生仓，按下了弹出按钮" %guess)
            print("逃生舱成功弹出，你赢了！")
            
            exit(0)


class Map(object):
    
    scenes = {
        "central_corridor": Central_Corridor(),
        "laser_weapon_armory": Laser_Weapon_Armory(),
        "the_bridge": The_Bridge(),
        "escape_pod": Escape_Pod(),
        "death": Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()