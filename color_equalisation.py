{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7f8f76a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def cal_equalisation(img,ratio):\n",
    "    Array = img * ratio\n",
    "    Array = np.clip(Array, 0, 255)\n",
    "    return Array\n",
    "\n",
    "def RGB_equalisation(img):\n",
    "    img = np.float32(img)\n",
    "    avg_RGB = []\n",
    "    for i in range(3):\n",
    "        avg = np.mean(img[:,:,i])\n",
    "        avg_RGB.append(avg)\n",
    "    # print('avg_RGB',avg_RGB)\n",
    "    a_r = avg_RGB[0]/avg_RGB[2]\n",
    "    a_g =  avg_RGB[0]/avg_RGB[1]\n",
    "    ratio = [0,a_g,a_r]\n",
    "    for i in range(1,3):\n",
    "        img[:,:,i] = cal_equalisation(img[:,:,i],ratio[i])\n",
    "    return img\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41d67ef3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
