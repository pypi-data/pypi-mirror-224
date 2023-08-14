import numpy as np
import sympy as sym
import math
import pyquaternion as pqu
import __future__


class Octonion:
    def __init__(self, x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7):
        self.x_0 = x_0
        self.x_1 = x_1
        self.x_2 = x_2
        self.x_3 = x_3
        self.x_4 = x_4
        self.x_5 = x_5
        self.x_6 = x_6
        self.x_7 = x_7
        self.norm = self.cal_norm()
        # self.conjugate = self.cal_conjugate()

    # self.inverse = self.cal_inverse()

    def Octon(self, x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7):  # define Octonion
        r_1 = [x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7]
        a_1 = np.array(r_1, float)
        return a_1

    def cal_norm(self):  # define norm
        b_1 = math.sqrt(
            self.x_0 ** 2
            + self.x_1 ** 2
            + self.x_2 ** 2
            + self.x_3 ** 2
            + self.x_4 ** 2
            + self.x_5 ** 2
            + self.x_6 ** 2
            + self.x_7 ** 2
        )
        return b_1

    def cal_conjugate(self):
        r_2 = [
            self.x_0,
            -(self.x_1),
            -(self.x_2),
            -(self.x_3),
            -(self.x_4),
            -(self.x_5),
            -(self.x_6),
            -(self.x_7),
        ]
        a_2 = np.array(r_2, float)
        return a_2

    @property
    def conjugate(self):
        conj = Octonion(
            self.x_0,
            -(self.x_1),
            -(self.x_2),
            -(self.x_3),
            -(self.x_4),
            -(self.x_5),
            -(self.x_6),
            -(self.x_7),
        )
        return conj

    def cal_multiply(self, x, y):  # define octonion multiplication
        # from pyquaternion import Quaternion
        a = pqu.Quaternion(x.x_0, x.x_1, x.x_2, x.x_3)
        b = pqu.Quaternion(x.x_4, x.x_5, x.x_6, x.x_7)
        c = pqu.Quaternion(y.x_0, y.x_1, y.x_2, y.x_3)
        d = pqu.Quaternion(y.x_4, y.x_5, y.x_6, y.x_7)
        a_1 = a * c - (d.conjugate) * b
        b_1 = (d * a) + (b * (c.conjugate))
        # print(np.array(a_1, float))
        # print(np.array(b_1, float))
        print(
            self.Octon(a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3])
        )
        xy = [a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]]
        xyz = np.array(xy, float)
        return xyz

    @property
    def inverse(self):  # define inverse
        # from pyquaternion import Quaternion
        b = self.cal_conjugate()
        # print("conjugate:{}".format(b))
        c = self.norm
        d = c ** 2
        e = [
            b[0] / d,
            b[1] / d,
            b[2] / d,
            b[3] / d,
            b[4] / d,
            b[5] / d,
            b[6] / d,
            b[7] / d,
        ]
        # x = np.array(e, float)
        x = Octonion(
            b[0] / d,
            b[1] / d,
            b[2] / d,
            b[3] / d,
            b[4] / d,
            b[5] / d,
            b[6] / d,
            b[7] / d,
        )
        return x

    def __div__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = x * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )

            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            bottom = float(y)
            addition = Octonion(
                x.x_0 / bottom,
                x.x_1 / bottom,
                x.x_2 / bottom,
                x.x_3 / bottom,
                x.x_4 / bottom,
                x.x_5 / bottom,
                x.x_6 / bottom,
                x.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __rdiv__(y, x):
        if isinstance(y, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = float(x) * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )
            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __truediv__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = x * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )

            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            bottom = float(y)
            addition = Octonion(
                x.x_0 / bottom,
                x.x_1 / bottom,
                x.x_2 / bottom,
                x.x_3 / bottom,
                x.x_4 / bottom,
                x.x_5 / bottom,
                x.x_6 / bottom,
                x.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __rtruediv__(y, x):
        if isinstance(y, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = float(x) * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )
            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __mul__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            a = pqu.Quaternion(x.x_0, x.x_1, x.x_2, x.x_3)
            b = pqu.Quaternion(x.x_4, x.x_5, x.x_6, x.x_7)
            c = pqu.Quaternion(y.x_0, y.x_1, y.x_2, y.x_3)
            d = pqu.Quaternion(y.x_4, y.x_5, y.x_6, y.x_7)
            a_1 = a * c - (d.conjugate) * b
            b_1 = (d * a) + (b * (c.conjugate))
            # xy = [a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]]
            # xyz = np.array(xy, float)
            mul = Octonion(
                a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]
            )
            return mul
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            mul = [
                x.x_0 * y,
                x.x_1 * y,
                x.x_2 * y,
                x.x_3 * y,
                x.x_4 * y,
                x.x_5 * y,
                x.x_6 * y,
                x.x_7 * y,
            ]
            multi = Octonion(
                mul[0], mul[1], mul[2], mul[3], mul[4], mul[5], mul[6], mul[7]
            )
            return multi
        raise NotImplementedError

    def __rmul__(y, x):
        # print(x)
        # print(y)
        if isinstance(y, Octonion):
            mul = [
                x * y.x_0,
                x * y.x_1,
                x * y.x_2,
                x * y.x_3,
                x * y.x_4,
                x * y.x_5,
                x * y.x_6,
                x * y.x_7,
            ]
            addition = Octonion(
                mul[0], mul[1], mul[2], mul[3], mul[4], mul[5], mul[6], mul[7]
            )
            return addition
        raise NotImplementedError

    def __add__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            total = [
                x.x_0 + y.x_0,
                x.x_1 + y.x_1,
                x.x_2 + y.x_2,
                x.x_3 + y.x_3,
                x.x_4 + y.x_4,
                x.x_5 + y.x_5,
                x.x_6 + y.x_6,
                x.x_7 + y.x_7,
            ]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            total = [x.x_0 + y, x.x_1, x.x_2, x.x_3, x.x_4, x.x_5, x.x_6, x.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __radd__(y, x):
        # print(x)
        # print(y)
        if isinstance(y, Octonion):
            total = [x + y.x_0, y.x_1, y.x_2, y.x_3, y.x_4, y.x_5, y.x_6, y.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __sub__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            total = [
                x.x_0 - y.x_0,
                x.x_1 - y.x_1,
                x.x_2 - y.x_2,
                x.x_3 - y.x_3,
                x.x_4 - y.x_4,
                x.x_5 - y.x_5,
                x.x_6 - y.x_6,
                x.x_7 - y.x_7,
            ]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            total = [x.x_0 - y, x.x_1, x.x_2, x.x_3, x.x_4, x.x_5, x.x_6, x.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __rsub__(y, x):
        # print(x)
        # print(y)
        if isinstance(y, Octonion):
            total = [x - y.x_0, -y.x_1, -y.x_2, -y.x_3, -y.x_4, -y.x_5, -y.x_6, -y.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __repr__(self):
        return "%+.4f %+0.4fi %+0.4fj %+0.4fk %+0.4fl %+0.4fil %+0.4fjl %+0.4fkl" % (
            self.x_0,
            self.x_1,
            self.x_2,
            self.x_3,
            self.x_4,
            self.x_5,
            self.x_6,
            self.x_7,
        )

    def __pow__(x, pow):
        if isinstance(x, Octonion):
            y = Octonion(x.x_0, x.x_1, x.x_2, x.x_3, x.x_4, x.x_5, x.x_6, x.x_7)
            while pow > 1:
                # print(y)
                a = pqu.Quaternion(x.x_0, x.x_1, x.x_2, x.x_3)
                b = pqu.Quaternion(x.x_4, x.x_5, x.x_6, x.x_7)
                c = pqu.Quaternion(y.x_0, y.x_1, y.x_2, y.x_3)
                d = pqu.Quaternion(y.x_4, y.x_5, y.x_6, y.x_7)
                a_1 = a * c - (d.conjugate) * b
                b_1 = (d * a) + (b * (c.conjugate))
                y = Octonion(
                    a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]
                )
                pow -= 1
            return y
        raise NotImplementedError

    def octquad(b,c):
        sym.init_printing()
        rho = '\u03C1'
        #theta,alpha,rho,beta,u,i,j,k,l,il,jl,kl=sym.symbols('theta alpha rho beta u i j k l il jl kl')
        theta,alpha,Rho,beta,u,i,j,k,l,il,jl,kl=sym.symbols("theta,alpha,Rho,beta,u,i,j,k,l,il,jl,kl")
        if b.x_1==0 and b.x_2==0 and b.x_3==0 and b.x_4==0 and b.x_5==0 and b.x_6==0 and b.x_7==0:
            if  c.x_1==0 and c.x_2==0 and c.x_3==0 and c.x_4==0 and c.x_5==0 and c.x_6==0 and c.x_7==0:
                d=4*c.x_0-b.x_0**2
                if d>0:
                    d_1=abs(math.sqrt(d/4))
                    print("Roots of the Octonionic Quadratic equation are:",-b.x_0/2,"+I")
                    print("where I is imaginary Octonion with norm equal to",d_1)
                else:
                    e=-d
                    print("Roots of the Octonionic Quadratic equation are:")
                    print((-b.x_0+math.sqrt(e))/2, "or",(-b.x_0-math.sqrt(e))/2 )
            else:
                r_1=((b.x_0**2-4*c.x_0)**2)+16*(c.x_1**2 + c.x_2**2 + c.x_3**2+c.x_4**2 + c.x_5**2 + c.x_6**2+c.x_7**2)
                r_2=b.x_0**2-4*c.x_0
                #print(rho/2)
                rho=sym.Symbol('\u03C1') 
                print("Roots are of the form:")
                print((-b.x_0/2)+(rho/2)-c.x_1*(i/rho)-c.x_2*(j/rho)-c.x_3*(k/rho)-c.x_4*(l/rho)-c.x_5*(il/rho)-c.x_6*(jl/rho)-c.x_7*(kl/rho))
                #print((-b.x_0/2)+('\u03C1 /2')-c.x_1*('i/\u03C1')-c.x_2*('j/\u03C1')-c.x_3*('k/\u03C1')-c.x_4*('l/\u03C1')-c.x_5*('il/\u03C1')-c.x_6*('jl/\u03C1')-c.x_7*('kl/\u03C1'))
                print("OR")
                print((-b.x_0/2)-(rho/2)+c.x_1*(i/rho)+c.x_2*(j/rho)+c.x_3*(k/rho)+c.x_4*(l/rho)+c.x_5*(il/rho)+c.x_6*(jl/rho)+c.x_7*(kl/rho))
                #print((-b.x_0/2)-('\u03C1/2')+c.x_1*('i/\u03C1')+c.x_2*('j/\u03C1')+c.x_3*('k/\u03C1')+c.x_4*('l/\u03C1')+c.x_5*('il/\u03C1')+c.x_6*('jl/\u03C1')+c.x_7*('kl/\u03C1'))
                h=math.sqrt(r_1)
                m=r_2+h
                p=math.sqrt(m/2)
                print("where \u03C1" ,  " = ",p)
                #print(rho) 
                #print("=",p)

                x_0=(-b.x_0/2)-(p/2)
                x_00=(-b.x_0/2)+(p/2)
                x_1=c.x_1/p
                x_2=c.x_2/p
                x_3=c.x_3/p
                x_4=c.x_4/p
                x_5=c.x_5/p
                x_6=c.x_6/p
                x_7=c.x_7/p
                q_1=Octonion(x_0,x_1,x_2,x_3,x_4,x_5,x_6,x_7)
                q_2=Octonion(x_00,-x_1,-x_2,-x_3,-x_4,-x_5,-x_6,-x_7)
                print("So, Roots of the Octonionic Quadratic equation can be written as: ",q_1," and ", q_2)
                #print(q_1,"and")
                #print(q_2)

        else:
            b_1=Octonion(0,b.x_1,b.x_2,b.x_3,b.x_4,b.x_5,b.x_6,b.x_7)
            b_11=Octonion(b.x_0/2,b.x_1,b.x_2,b.x_3,b.x_4,b.x_5,b.x_6,b.x_7)
            c_11=(b.x_0/2)*(b_11)
            c_1=c+(-1)*c_11
            
            B=(b_1.norm)**2 +2*c_1.x_0
            E=(c_1.norm)**2
            
            D_1=(b_1.conjugate)*(c_1)
            D=2*D_1.x_0
         
            if D==0:
                if B>=2*math.sqrt(E) or B<= -2*math.sqrt(E):
                    T=0
                    N_1=(B+math.sqrt(B**2 -4*E))/2
                    N_2=(B-math.sqrt(B**2 -4*E))/2
                    Q=b_1.inverse
                    c_111=c_1-N_1
                    xx_1=Q*c_111
                    xx_3= -(b.x_0/2)+(-1)*xx_1
                    d_111=c_1-N_2
                    xx_2=Q*d_111
                    xx_4=-(b.x_0/2)+(-1)*xx_2
                    print("Roots of the Octonionic Quadratic equation can be written as: ",xx_3, " and ", xx_4)
                    #print(xx_3,"and")
                    #print(xx_4)
                    
                else:
                    T_1=math.sqrt(2*math.sqrt(E)-B)
                    T_2=-math.sqrt(2*math.sqrt(E)-B)
                    N=math.sqrt(E)

                    Q_1=(T_1+b_1).inverse
                    Q_2=(T_2+b_1).inverse
                  
                    c_111=c_1-N
                    xx_1=Q_1*c_111
                    
                    xx_3=-(b.x_0/2)+(-1)*xx_1
                    xx_2=Q_2*c_111
                    
                    xx_4=-(b.x_0/2)+(-1)*xx_2
                    print("Roots of the Octonionic Quadratic equation can be written as: ",xx_3, " and ", xx_4)
                    #print(xx_3,"and")
                    #print(xx_4)
            else: 

                p=np.poly1d([1,2*B,B**2 -4*E,-(D**2)])
                rootsp=p.r

                var=[0,1,2]

                for n in var:
                    #print(rootsp[n])
                    if rootsp[n]>0 :
                        root=rootsp[n]

                T_1=math.sqrt(root)
                T_2=-math.sqrt(root)
                N_1=(T_1**3 +B*T_1+D)/(2*T_1)
                N_2=(T_2**3 +B*T_2+D)/(2*T_2)
                Q_1=(T_1+b_1).inverse
                Q_2=(T_2+b_1).inverse
                c_111=c_1-N_1
                d_111=c_1-N_2
                xx_1=Q_1*c_111
                xx_3=-b.x_0/2 +(-1)*xx_1    
                xx_2=Q_2*d_111
                xx_4=-b.x_0/2+(-1)*xx_2 
                print("Roots of the Octonionic Quadratic equation can be written as: ",xx_3," and ",xx_4)
                #print(xx_3,"and")
                #print(xx_4)

###function verification### 
#b=Octonion(-1,0,0,0,0,0,0,0)
#c=Octonion(0,0,0,0,1,0,0,0)
#Octonion.octquad(b,c)
#b=Octonion(0,0,0,0,1,0,0,0)
#c=Octonion(0,0,1,0,0,0,0,0)
#Octonion.octquad(b,c)               
#b=Octonion(0,0,0,0,0,0,0,0)
#c=Octonion(1,0,0,0,0,0,0,0)
#Octonion.octquad(b,c)
#b=Octonion(5,0,0,0,0,0,0,0)
#c=Octonion(6,0,0,0,0,0,0,0)
#Octonion.octquad(b,c)
#b = Octonion(1, 0, 0, 0, 0, 0, 1, 1)
# c = Octonion(1, 0, 0, 0, 0, 0, 0, 1)
#print(b ** 300)
# print(b ** 3)
# print('b*b*b')
# print(b*b*b)
# print('c**4')
# print(c ** 4)
# print('c*c*c*c')
# print(c*c*c*c)


# print(b / c)
# print(2 / b)
# print(b / 2)
# print(b * 5)
# print(5 * b)
# print(2 / b)

# print(b * c)
# print(b * 2)
# print(2 * b)
# print(c)
# print(b.conjugate)
# print(b.inverse)
# print(2 * b)
# print(b + c)
# print(b - c)
# print(2 + b)
# print(b + 2)
# print(b - 2)
# print(2 - b)


# octonion.oct_quad(0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0)

# octonion.oct_quad(2/3,0,0,-1/3,-1/3,0,0,0,-1/3,0,0,2/3,2/3,0,0,0)

# octonion.oct_quad(0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0)

# octonion.oct_quad(0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8)

# octonion.oct_quad(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
