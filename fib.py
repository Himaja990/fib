{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "234a89e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the value:50\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "8\n",
      "13\n",
      "21\n",
      "34\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Write a Python program to get the Fibonacci series between 0 to 50\n",
    "\n",
    "\n",
    "\n",
    "Note : The Fibonacci Sequence is the series of numbers :\n",
    "\n",
    "0, 1, 1, 2, 3, 5, 8, 13, 21, ....\n",
    "\n",
    "Every next number is found by adding up the two numbers before it.\n",
    "\n",
    "Expected Output : 1 1 2 3 5 8 13 21 34\n",
    "\n",
    "'''\n",
    "\n",
    "num=int(input(\"enter the value:\"))\n",
    "a=0\n",
    "b=1\n",
    "if num==1:\n",
    "    print(a)\n",
    "else:\n",
    "    print(b)\n",
    "    for i in range(2,num):\n",
    "        c=a+b\n",
    "        a=b\n",
    "        b=c\n",
    "        if c<num :\n",
    "            print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e08e463b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15584b71",
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
