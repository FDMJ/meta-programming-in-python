my_global = 10 #global scope

def fn1():
    enclosed_v = 8 #enclosed scope

    def fn2():
        local_v = 5 #local scope
        print('Access to Global', my_global)
        print('Access to enclosed', enclosed_v)
    fn2()

fn1()