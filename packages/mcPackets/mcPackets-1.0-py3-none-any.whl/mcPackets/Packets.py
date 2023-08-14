import os

import nbtlib

import mcPackets.packetFile.packetFeile
from mcPackets import algorithm

class _repeat:
    def __init__(self):
        pass

    def parameter_conversion(self, S: str) -> int:
        """
        :param S: 传入参数1.13或1.16.5
        :return: 返回为1130或1165
        """
        parts = S.split('.')
        if len(parts) == 1:
            number = parts[0] + parts[1] + '0'
        else:
            number = parts[0] + parts[1] + parts[2]
        return int(number)

class _path_location:
    def __init__(self,
                 namespace: str,
                 absolute_path: str,
                 packet_name: str,
                 path: str
                 ):

        self.packet_Naming = {
            "Namespace": namespace
        }
        self.path = path
        self.packet_name = packet_name
        self.absolute_path = absolute_path
        self.repeat = _repeat()


        self.Game_version = None

        self.minimum_Game_version = 1130
        # 17w43a(1.13) 加入了数据包
        self.whether_build = None
        # 版本低于1.13 则不准生成

    def location(self):
        """
        此函数用于定位，地图或者数据包
        path 参数为  为地图路径或者数据包路径
                    地图session.lock文件 或者
                    数据包pack.mcmeta文件
        """

        # 当用户给定一个文件夹路径时，调用这个函数
        def folder(path):
            def _(path: str):
                # 文件夹递归
                for i in os.listdir(path):
                    absolute_path = f'{path}/{i}'
                    if os.path.isdir(absolute_path) and i in folder_Endings:
                        if os.path.isfile(f'{path}/{file_Endings[1]}'):
                            return f'{path}/{file_Endings[1]}'

                    if os.path.isfile(absolute_path) and i in file_Endings:
                        return absolute_path
                v = len(path.split('/'))
                if v in [0, 1, 2]:
                    return False

                else:
                    return _(os.path.dirname(path))

            v = _(path)
            return v

        # 当用户给定一个文件路径时，调用这个函数
        def file(path: str):
            fill_Endings = path.split('/')[-1]
            if fill_Endings in file_Endings:
                for i in file_Endings:
                    if i != fill_Endings:
                        continue
                    if os.path.isfile(path):
                        return path
            else:
                # 使用文件递归操作
                v = folder(os.path.dirname(path))
                return v

        if not os.path.exists(self.path):
            # 验证path
            return None

        file_Endings = [
            'session.lock', 'pack.mcmeta'
        ]
        folder_Endings = [
            'datapacks'
        ]

        if not os.path.isdir(self.path):
            top = file(self.path)

        else:
            top = folder(self.path)

        if top in [False, None]:
            raise Exception("path参数错误!无法定位地图或者数据包,可以使用absolute_path参数定位")

        else:
            fill_Endings = top.split('/')[-1]
            if fill_Endings == 'pack.mcmeta':
                _ = top
                for i in range(3):
                    os.path.dirname(_)

                return f"{_}/session.lock", top
            else:
                v = [
                    'datapacks', self.packet_name, 'pack.mcmeta'
                ]
                fill_Endings = top
                _ = True
                for i in v:
                    fill_Endings = f"{os.path.dirname(fill_Endings)}/{i}"
                    if not os.path.exists(fill_Endings):
                        _ = False

                if _ == False:
                    return top, None
                return top, fill_Endings

    def absolute_location(self):
        v = self.absolute_path.split('/')[-1]
        if not v == 'session.lock':
            raise Exception("absolute_path参数错误!无法定位地图, 文件名不一")
        if not os.path.isfile(self.absolute_path):
            raise Exception("absolute_path参数错误!无法定位地图, 无文件")

        return self.absolute_path, None

    def packet_version(self, S: int) -> int:
        l1 = [
            i for i in range(3, 16)
        ]
        l2 = [
            1130, 1144, 1161, 1165, 1171, 1181, 1182, 1193, 1194, 1194, 1200, 1200, 1200
        ]

        _ = l1[l2.count(algorithm.find_nearest_number(l2, S))+1]

        return _


    def Generate_packets(self, path, packet_name, namespace):
        if not self.whether_build == True:
            raise Exception("版本低于1.13！")

        if os.path.isdir(path):
            os.mkdir(f"{path}/{packet_name}")
            with open(f"{path}/{packet_name}/pack.mcmeta", mode='w', encoding='utf-8') as f:
                _ = {
                    "pack": {
                        "pack_format": self.packet_version(self.whether_build),
                        "description": "The default data for Minecraft"
                    }
                }

    def level_dat(self, path):
        # 游戏版本获取
        level_data = nbtlib.load(path) # 读取level.dat文件
        # 获取游戏版本
        spawn_position = level_data["Data"]["Version"]["Name"]
        spawn_position = self.repeat.parameter_conversion(str(spawn_position))
        self.Game_version = spawn_position
        self.whether_build = True if not spawn_position - 1130 < 0 else False
        return spawn_position

class packets:
    def __init__(self,
                 path: str = None,
                 absolute_path: str = False,
                 packet_name: str = 'test',
                 namespace: str = 'lock',
                 ):
        """
        :param path:
                path 参数为  为地图路径或者数据包路径
                    地图session.lock文件 或者
                    数据包pack.mcmeta文件
        :param absolute_path:
                absolute_path 参数为 绝对定位,给出的路径必须是 地图session.lock文件
                优先定位,当参数定位出来后则不再运行path定位
        :param packet_name:
            数据包名称
        :param namespace:
            命名空间
        """

        path = None if path == None else path.replace('\\', '/').replace('//', '/')
        absolute_path = False if absolute_path != None else absolute_path.replace('\\', '/').replace('//', '/')
        # 参数转换
        self._location = _path_location(
            # 对核心类初始化
            **{
            "namespace": namespace,
            "absolute_path": absolute_path,
            "packet_name": packet_name,
            "path": path
            }
        )

        self.errorMessage: str = 'None'
        self.code_errorMessage: str = "None"

        # .lock .mcmeta 路径
        # 定位地图
        if absolute_path == False:
            self.path_session, self.pack_mcmeta = self._location.location()
        else:
            self.path_session, self.pack_mcmeta = self._location.absolute_location()

        if self.path_session != None:
            # 游戏版本
            self.path_session = os.path.dirname(self.path_session)
            v = self._location.level_dat(f"{self.path_session}/level.dat")

    # 创建数据包
    def createPackets(self, packet_name: str=None, namespace: str=None, description: str='hello py!'):
        """
        创建数据包
        :param packet_name: 是数据包名
        :param namespace: 空间名
        :param description:
            pack.mcmeta文件中的描述
        :return:
        """
        packet_name = packet_name if not packet_name == None else self._location.packet_name
        namespace = namespace if not namespace == None else self._location.packet_Naming["Namespace"]

        if self.path_session == None:
            self.__errorMessage("path_session")
            return

        structure_tree =  mcPackets.packetFeile.primitiveness(packet_name, namespace,
                    mcPackets.packetFeile.pack_mcmeta(self._location.packet_version(
                        self._location.Game_version), description))
        _, f = mcPackets.algorithm.create_folder_with_json_file(structure_tree,
                f"{self.path_session}/{mcPackets.packetFeile.dataClass_Name['datapacks']}")

        if _ == False:
            self._verify(f)
            return False

        return True

    # 游戏函数
    def functions(self):
        pass

    # 游戏配方
    def recipes(self):
        pass

    # 游戏结构
    def structures(self):
        pass

    # 游戏进度
    def advancements(self):
        pass

    # 错误
    def _verify(self, f, whether: bool=False):
        def _(f, name, text):
            self.__errorMessage(text)
            if whether == True:
                raise f(name, text)

        f, name, text = f
        vf = {
            "FileNotFoundError": (FileNotFoundError,  "文件错误!")
        }
        [_(f, name, text) for i in vf if vf[i][0] ==f]

    # 错误信息
    def __errorMessage(self, s: str, code_errorMessage=None):
        self.errorMessage = s
        self.code_errorMessage = code_errorMessage if code_errorMessage == None else self.code_errorMessage
        return True

    # 数据包 参数修改
    def parameter_modification(self, **key):
        """
        参数修改
        """
        def _(
                packet_name = self._location.packet_name,
                namespace = self._location.packet_Naming["Namespace"]
        ):
            self._location.packet_name = packet_name
            self._location.packet_Naming["Namespace"] = namespace

        _(**key)

