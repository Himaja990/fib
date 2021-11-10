{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8ba12cc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "print even count: 4\n",
      "print odd count: 5\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Write a Python program to count the number of even and odd numbers from a series of numbers.\n",
    "\n",
    "\n",
    "\n",
    "Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) \n",
    "\n",
    "Expected Output :\n",
    "\n",
    "Number of even numbers : 5\n",
    "\n",
    "Number of odd numbers : 4\n",
    "\n",
    "'''\n",
    "\n",
    "n=(1,2,3,4,5,6,7,8,9)\n",
    "\n",
    "even_count , odd_count=0,0\n",
    "\n",
    "for n in num:\n",
    "\n",
    "    if n % 2==0:\n",
    "        even_count+=1\n",
    "    else:\n",
    "        odd_count+=1\n",
    "print(\"print even count:\",even_count)\n",
    "print(\"print odd count:\",odd_count)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a71b40d",
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
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
