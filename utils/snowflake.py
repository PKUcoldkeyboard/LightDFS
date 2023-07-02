from datetime import datetime
import threading

tlock = threading.Lock()

machineId = 0  # 机器ID
datacenterId = 0  # 数据ID

sequence = 0  # 计数从零开始

twepoch = 687888001020  # 唯一时间随机量

machineIdBits = 5  # 机器码位数
datacenterIdBits = 5  # 数据位数
maxMachineId = -1 ^ -1 << machineIdBits  # 最大机器ID
maxDatacenterId = -1 ^ (-1 << datacenterIdBits)  # 最大数据ID

sequenceBits = 12  # 计数器位数，12个位用来保存计数码
machineIdShift = sequenceBits  # 机器码数据左移位数，就是后面计数器占用的位数
datacenterIdShift = sequenceBits + machineIdBits
timestampLeftShift = sequenceBits + machineIdBits + \
    datacenterIdBits  # 时间戳左移动位数就是机器码+计数器总位数+数据位数
sequenceMask = -1 ^ -1 << sequenceBits  # 一微秒内可以产生计数，如果达到该值则等到下一微妙在进行生成

lastTimestamp = -1  # 最后时间戳


def getTimestamp():
    return int(datetime.now().timestamp() * 1000)


def getNextTimestamp(lastTimestamp):
    timestamp = getTimestamp()
    while timestamp <= lastTimestamp:
        timestamp = getTimestamp()
    return timestamp


def getId():
    '''
    线程安全的
    '''
    # plock.acquire()
    with tlock:
        global lastTimestamp, sequence
        timestamp = getTimestamp()
        if lastTimestamp == timestamp:
            # 同一微妙中生成ID
            sequence = (sequence + 1) & sequenceMask  # 用&运算计算该微秒内产生的计数是否已经到达上限
            if sequence == 0:
                # 一微妙内产生的ID计数已达上限，等待下一微妙
                timestamp = getNextTimestamp(lastTimestamp)
        else:
            # 不同微秒生成ID
            sequence = 0

        if timestamp < lastTimestamp:
            raise Exception("时间戳比上一次生成ID时时间戳还小，故异常")
        lastTimestamp = timestamp  # 把当前时间戳保存为最后生成ID的时间戳
        # print(((timestamp - twepoch) << timestampLeftShift), sequence)#, file=open('t.txt', 'a'))
        Id = ((timestamp - twepoch) << timestampLeftShift)\
            | (datacenterId << datacenterIdShift)\
            | (machineId << machineIdShift)\
            | sequence
        # tlock.release()
        # plock.release()
        return Id
