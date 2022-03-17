{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP+wSMj9aGJHlHeFUSTwTn1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Avinash-099/python-programs-/blob/main/Untitled2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "F2us2oeuf2vi"
      },
      "outputs": [],
      "source": [
        "## CONVERTING INT TO STRING ,FLOAT ,BOOLEAN, COMPLEX .\n",
        "a=10 \n",
        "print(a)\n",
        "print(type(a))\n",
        "b=str(a)\n",
        "print(b)\n",
        "print(type(b))\n",
        "c=bool(a)\n",
        "print(c)\n",
        "print(type(c))\n",
        "c=complex(a)\n",
        "print(c)\n",
        "print(type(a))\n",
        "​\n",
        "10\n",
        "<class 'int'>\n",
        "10\n",
        "<class 'str'>\n",
        "True\n",
        "<class 'bool'>\n",
        "(10+0j)\n",
        "<class 'int'>\n",
        "# CONVERTING STRING TO INT ,FLOAT ,BOOLEAN, COMPLEX .\n",
        "a='10'\n",
        "print(type(a))\n",
        "print(a)\n",
        "b=int(a)\n",
        "print(b)\n",
        "​\n",
        "#cannot covert alphabet into integers ,only digits can be coverted into \n",
        "#instead of alphabets give numbers between 0-9\n",
        "e=float(a)\n",
        "print(e)\n",
        "print(type(e))\n",
        "f=bool(a)\n",
        "print(f)\n",
        "print(type(f))\n",
        "g=complex(a)\n",
        "print(g)\n",
        "print(type(g))\n",
        "​\n",
        "<class 'str'>\n",
        "10\n",
        "10\n",
        "10.0\n",
        "<class 'float'>\n",
        "True\n",
        "<class 'bool'>\n",
        "(10+0j)\n",
        "<class 'complex'>\n",
        "# # CONVERTING FLOAT  TO INT ,STRING ,BOOLEAN, COMPLEX .\n",
        "a=10.5\n",
        "print(a)\n",
        "print(type(a))\n",
        "b=str(a)\n",
        "print(b)\n",
        "print(type(b))\n",
        "c=bool(a)\n",
        "print(c)\n",
        "print(type(c))\n",
        "c=complex(a)\n",
        "print(c)\n",
        "print(type(c))\n",
        "​\n",
        "10.5\n",
        "<class 'float'>\n",
        "10.5\n",
        "<class 'str'>\n",
        "True\n",
        "<class 'bool'>\n",
        "(10.5+0j)\n",
        "<class 'complex'>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "0zc7EItFs-GF"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
