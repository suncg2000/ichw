{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "TurtleGraphicsError",
     "evalue": "bad color string: orange",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTurtleGraphicsError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-eb284d3da65a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     34\u001b[0m     \u001b[0moval\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.05\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'red'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mt4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m     \u001b[0moval\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.05\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"pink\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mt1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 36\u001b[1;33m     \u001b[0moval\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.05\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1500\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'orange'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mt2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     37\u001b[0m     \u001b[0moval\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.05\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2000\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"blue\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mt3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     38\u001b[0m     \u001b[0moval\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0.07\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3500\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"gray\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mt5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-7-eb284d3da65a>\u001b[0m in \u001b[0;36moval\u001b[1;34m(e, p, c, t, o, r)\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0moval\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mp\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mt\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mo\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mr\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m     \u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'circle'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 16\u001b[1;33m     \u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcolor\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     17\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mr\u001b[0m\u001b[1;33m//\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m         \u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpenup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32me:\\python\\lib\\turtle.py\u001b[0m in \u001b[0;36mcolor\u001b[1;34m(self, *args)\u001b[0m\n\u001b[0;32m   2214\u001b[0m             \u001b[1;32melif\u001b[0m \u001b[0ml\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2215\u001b[0m                 \u001b[0mpcolor\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfcolor\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2216\u001b[1;33m             \u001b[0mpcolor\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_colorstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpcolor\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2217\u001b[0m             \u001b[0mfcolor\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_colorstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfcolor\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2218\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpencolor\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpcolor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfillcolor\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfcolor\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32me:\\python\\lib\\turtle.py\u001b[0m in \u001b[0;36m_colorstr\u001b[1;34m(self, args)\u001b[0m\n\u001b[0;32m   2694\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2695\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_colorstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2696\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscreen\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_colorstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2697\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2698\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_cc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32me:\\python\\lib\\turtle.py\u001b[0m in \u001b[0;36m_colorstr\u001b[1;34m(self, color)\u001b[0m\n\u001b[0;32m   1156\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mcolor\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1157\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1158\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mTurtleGraphicsError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"bad color string: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcolor\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1159\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1160\u001b[0m             \u001b[0mr\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mg\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcolor\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTurtleGraphicsError\u001b[0m: bad color string: orange"
     ]
    }
   ],
   "source": [
    "'''planets.py:a model of the solar system\n",
    "__auther__=\"sun chen'geng\"\n",
    "__pkuid__  = \"1800011825\"\n",
    "__email__  = \"1800011825@pku.edu.cn\"\n",
    "'''\n",
    "import turtle\n",
    "t0=turtle.Pen()\n",
    "t0.shape('circle')\n",
    "t0.color('yellow')\n",
    "t0.stamp()\n",
    "\n",
    "import math\n",
    "\n",
    "def oval(e,p,c,t,o,r):\n",
    "    t.shape('circle')\n",
    "    t.color(c)\n",
    "    if r//7==0:\n",
    "        t.penup()\n",
    "        t.goto(e*p/(1-e),0)\n",
    "        t.pendown()\n",
    "    else:\n",
    "        x=(e*p)/(1-e*math.cos(math.radians(r/(o))))\n",
    "        if r%7==o:\n",
    "            t.goto(x*(math.cos(math.radians(r/(o)))),x*(math.sin(math.radians(r/(o)))))\n",
    "    return t\n",
    "\n",
    "t1=turtle.Pen()\n",
    "t2=turtle.Pen()\n",
    "t3=turtle.Pen()\n",
    "t4=turtle.Pen()\n",
    "t5=turtle.Pen()\n",
    "t6=turtle.Pen()\n",
    "for y in range(10000):\n",
    "    oval(0.05,3000,'red',t4,4,y)\n",
    "    oval(0.05,1000,\"pink\",t1,1,y)\n",
    "    oval(0.05,1500,'orange',t2,2,y)\n",
    "    oval(0.05,2000,\"blue\",t3,3,y)\n",
    "    oval(0.07,3500,\"gray\",t5,5,y)\n",
    "    oval(0.08,4000,\"green\",t6,6,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
