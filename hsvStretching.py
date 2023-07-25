{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "75574e9b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'global_Stretching'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [9], line 7\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msys\u001b[39;00m\n\u001b[0;32m      5\u001b[0m sys\u001b[38;5;241m.\u001b[39mpath\u001b[38;5;241m.\u001b[39mappend(\u001b[38;5;124mr\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mC:\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mUsers\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mSaptarshi\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mProject\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m----> 7\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mglobal_Stretching\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m global_stretching\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m  \u001b[38;5;21mHSVStretching\u001b[39m(sceneRadiance):\n\u001b[0;32m     11\u001b[0m     sceneRadiance \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39muint8(sceneRadiance)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'global_Stretching'"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "from skimage.color import rgb2hsv,hsv2rgb\n",
    "import numpy as np\n",
    "import sys\n",
    "sys.path.append(r'C:\\Users\\Saptarshi\\Project')\n",
    "\n",
    "from global_Stretching import global_stretching\n",
    "\n",
    "\n",
    "def  HSVStretching(sceneRadiance):\n",
    "    sceneRadiance = np.uint8(sceneRadiance)\n",
    "    height = len(sceneRadiance)\n",
    "    width = len(sceneRadiance[0])\n",
    "    img_hsv = rgb2hsv(sceneRadiance)\n",
    "    h, s, v = cv2.split(img_hsv)\n",
    "    img_s_stretching = global_stretching(s, height, width)\n",
    "    img_v_stretching = global_stretching(v, height, width)\n",
    "\n",
    "    labArray = np.zeros((height, width, 3), 'float64')\n",
    "    labArray[:, :, 0] = h\n",
    "    labArray[:, :, 1] = img_s_stretching\n",
    "    labArray[:, :, 2] = img_v_stretching\n",
    "    img_rgb = hsv2rgb(labArray) * 255\n",
    "\n",
    "    # img_rgb = np.clip(img_rgb, 0, 255)\n",
    "\n",
    "    return img_rgb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b00e4c0",
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
