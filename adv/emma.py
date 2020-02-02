import adv_test
from adv import *
from slot.d import *
from slot.a import *
from module import energy

def module():
    return Emma

class Emma(Adv):
    a1 = ('bt',0.25)
    a3 = ('primed_att', 0.05)

    conf = {}
    conf['slots.d'] = Cerberus()

    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = HG()+JotS()
            this.conf['acl'] = """
                        `s3, not this.s3_buff_on
                        `s1
                        """
        else:
            this.conf.slot.a = HG()+FWHC()
            this.conf['acl'] = """
                        `s3, not this.s3_buff_on
                        `s1, fsc
                        `fs, seq=5
                        """

    def init(this):
        comment = 'no s2'
        energy.Energy(this,{},{})
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc


    def c_s1_proc(this, e):
        Teambuff('s2',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s2',0.25,15).on()

    def s2_proc(this, e):
        Event('defchain')()

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=-2)

