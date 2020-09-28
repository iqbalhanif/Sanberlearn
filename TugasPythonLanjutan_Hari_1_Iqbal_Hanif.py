{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "TugasPythonLanjutan_Hari_1_Iqbal Hanif.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyO6vSPkasV2TOCNnYHOn763",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/iqbalhanif/Sanberlearn/blob/master/TugasPythonLanjutan_Hari_1_Iqbal_Hanif.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "30j47d6WGNCb"
      },
      "source": [
        "#1. Pengalaman saya menggunakan python adalah ketika saya mengikuti kelas python beginner dari sanberlearn\n",
        "#2. Ada kelas lanjutan lagi tentang python for data science untuk bidang image recognition atau video analytics\n",
        "#3. Kodingannya dibawah ini"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OSfZkbLvGt3i",
        "outputId": "d5b6e10c-c8f6-4446-89b2-415c4e32409b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 100
        }
      },
      "source": [
        "class manipulasi:\n",
        "  def __init__(self):\n",
        "    self.kalimat = input(\"data = \")\n",
        "  \n",
        "  def kapital(self):\n",
        "    print(self.kalimat.capitalize())\n",
        "  \n",
        "  def kecil(self):\n",
        "    print(self.kalimat.lower())\n",
        "  \n",
        "  def besar(self):\n",
        "    print(self.kalimat.upper())\n",
        "\n",
        "  def pisah(self):\n",
        "    print(self.kalimat.split())\n",
        "\n",
        "tes = manipulasi()\n",
        "tes.kapital()\n",
        "tes.kecil()\n",
        "tes.besar()\n",
        "tes.pisah()\n"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "data = saya tinggal di Indonesia\n",
            "Saya tinggal di indonesia\n",
            "saya tinggal di indonesia\n",
            "SAYA TINGGAL DI INDONESIA\n",
            "['saya', 'tinggal', 'di', 'Indonesia']\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}