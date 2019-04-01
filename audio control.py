
from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = "e0:14:d0:63:3d:d0"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=True)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(5)
'''
    if (mambo.sensors.flying_state != "emergency"):
        print("flying state is %s" % mambo.sensors.flying_state)
        print("Flying direct: going up")
        mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=10, duration=1)
        mambo.smart_sleep(5)
        
        print("flip left")
        print("flying state is %s" % mambo.sensors.flying_state)
        success = mambo.flip(direction="left")
        print("mambo flip result %s" % success)
        mambo.smart_sleep(5)

        print("flip right")
        print("flying state is %s" % mambo.sensors.flying_state)
        success = mambo.flip(direction="right")
        print("mambo flip result %s" % success)
        mambo.smart_sleep(5)

        print("flip front")
        print("flying state is %s" % mambo.sensors.flying_state)
        success = mambo.flip(direction="front")
        print("mambo flip result %s" % success)
        mambo.smart_sleep(5)

        print("flip back")
        print("flying state is %s" % mambo.sensors.flying_state)
        success = mambo.flip(direction="back")
        print("mambo flip result %s" % success)
        mambo.smart_sleep(5)
        
        print("landing")
        print("flying state is %s" % mambo.sensors.flying_state)
        mambo.safe_land(5)
        mambo.smart_sleep(5)
        
    print("disconnect")
    mambo.disconnect()

while(True):
    # 请说出语音指令，例如["向上", "向下", "向左", "向右"]
    print("\n\n==================================================")
    print("Please tell me the command(limit within 3 seconds):")
    result=baidu_aip.voice_recognize();
    if(result=="起飞"):
        print("taking off!")
        mambo.safe_takeoff(5)
        print("Control End...")
    if result=="退出": # 如果是"退出"指令则结束程序
        break;
    time.sleep(1) # 延时1秒
'''
