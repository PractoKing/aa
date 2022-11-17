{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "Name : Aniket Gore\n",
        "\n",
        "Roll No.: 9026\n",
        "\n",
        "Assignment 1 : Predict the price of the Uber ride"
      ],
      "metadata": {
        "id": "PBKP8lwpXFO6"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "oHYec-jCqPp1"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"uber.csv\")"
      ],
      "metadata": {
        "id": "YLKwK3v9sL3s"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "ESlI6iBqsUon",
        "outputId": "9823aefc-db52-4b5c-c204-74af187858bb"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0                            key  fare_amount  \\\n",
              "0    24238194    2015-05-07 19:52:06.0000003          7.5   \n",
              "1    27835199    2009-07-17 20:04:56.0000002          7.7   \n",
              "2    44984355   2009-08-24 21:45:00.00000061         12.9   \n",
              "3    25894730    2009-06-26 08:22:21.0000001          5.3   \n",
              "4    17610152  2014-08-28 17:47:00.000000188         16.0   \n",
              "\n",
              "           pickup_datetime  pickup_longitude  pickup_latitude  \\\n",
              "0  2015-05-07 19:52:06 UTC        -73.999817        40.738354   \n",
              "1  2009-07-17 20:04:56 UTC        -73.994355        40.728225   \n",
              "2  2009-08-24 21:45:00 UTC        -74.005043        40.740770   \n",
              "3  2009-06-26 08:22:21 UTC        -73.976124        40.790844   \n",
              "4  2014-08-28 17:47:00 UTC        -73.925023        40.744085   \n",
              "\n",
              "   dropoff_longitude  dropoff_latitude  passenger_count  \n",
              "0         -73.999512         40.723217              1.0  \n",
              "1         -73.994710         40.750325              1.0  \n",
              "2         -73.962565         40.772647              1.0  \n",
              "3         -73.965316         40.803349              3.0  \n",
              "4         -73.973082         40.761247              5.0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-669a5dbe-a67b-4b05-b89f-6b01d176e450\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>key</th>\n",
              "      <th>fare_amount</th>\n",
              "      <th>pickup_datetime</th>\n",
              "      <th>pickup_longitude</th>\n",
              "      <th>pickup_latitude</th>\n",
              "      <th>dropoff_longitude</th>\n",
              "      <th>dropoff_latitude</th>\n",
              "      <th>passenger_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>24238194</td>\n",
              "      <td>2015-05-07 19:52:06.0000003</td>\n",
              "      <td>7.5</td>\n",
              "      <td>2015-05-07 19:52:06 UTC</td>\n",
              "      <td>-73.999817</td>\n",
              "      <td>40.738354</td>\n",
              "      <td>-73.999512</td>\n",
              "      <td>40.723217</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>27835199</td>\n",
              "      <td>2009-07-17 20:04:56.0000002</td>\n",
              "      <td>7.7</td>\n",
              "      <td>2009-07-17 20:04:56 UTC</td>\n",
              "      <td>-73.994355</td>\n",
              "      <td>40.728225</td>\n",
              "      <td>-73.994710</td>\n",
              "      <td>40.750325</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>44984355</td>\n",
              "      <td>2009-08-24 21:45:00.00000061</td>\n",
              "      <td>12.9</td>\n",
              "      <td>2009-08-24 21:45:00 UTC</td>\n",
              "      <td>-74.005043</td>\n",
              "      <td>40.740770</td>\n",
              "      <td>-73.962565</td>\n",
              "      <td>40.772647</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>25894730</td>\n",
              "      <td>2009-06-26 08:22:21.0000001</td>\n",
              "      <td>5.3</td>\n",
              "      <td>2009-06-26 08:22:21 UTC</td>\n",
              "      <td>-73.976124</td>\n",
              "      <td>40.790844</td>\n",
              "      <td>-73.965316</td>\n",
              "      <td>40.803349</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>17610152</td>\n",
              "      <td>2014-08-28 17:47:00.000000188</td>\n",
              "      <td>16.0</td>\n",
              "      <td>2014-08-28 17:47:00 UTC</td>\n",
              "      <td>-73.925023</td>\n",
              "      <td>40.744085</td>\n",
              "      <td>-73.973082</td>\n",
              "      <td>40.761247</td>\n",
              "      <td>5.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-669a5dbe-a67b-4b05-b89f-6b01d176e450')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-669a5dbe-a67b-4b05-b89f-6b01d176e450 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-669a5dbe-a67b-4b05-b89f-6b01d176e450');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Preprocessing the Dataset**"
      ],
      "metadata": {
        "id": "x1tQc7HEsffm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1epew4xwsnV-",
        "outputId": "ebdd2414-91f8-40e1-90a3-1af3c46b0f0c"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Unnamed: 0           0\n",
              "key                  0\n",
              "fare_amount          0\n",
              "pickup_datetime      0\n",
              "pickup_longitude     0\n",
              "pickup_latitude      0\n",
              "dropoff_longitude    0\n",
              "dropoff_latitude     0\n",
              "passenger_count      1\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#dropping rows with missing values\n",
        "\n",
        "df.dropna(inplace = True)"
      ],
      "metadata": {
        "id": "_8e-7LwBs1em"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vbOfhjN8s4Hf",
        "outputId": "a26bb673-22dd-43b2-dcbe-fcf8835007ce"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Unnamed: 0           0\n",
              "key                  0\n",
              "fare_amount          0\n",
              "pickup_datetime      0\n",
              "pickup_longitude     0\n",
              "pickup_latitude      0\n",
              "dropoff_longitude    0\n",
              "dropoff_latitude     0\n",
              "passenger_count      0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#dropping unwanted columns\n",
        "\n",
        "df.drop(labels='Unnamed: 0',axis=1,inplace=True)\n",
        "df.drop(labels='key',axis=1,inplace=True)\n",
        "df.drop(labels='pickup_datetime',axis=1,inplace=True)"
      ],
      "metadata": {
        "id": "R_hVk5Hes7Ca"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "XwRjXP_Mtviv",
        "outputId": "32a1f469-9796-4ba7-fc63-ee55efcf47ba"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        fare_amount  pickup_longitude  pickup_latitude  dropoff_longitude  \\\n",
              "count  26781.000000      26781.000000     26781.000000       26781.000000   \n",
              "mean      11.409123        -72.562169        39.940917         -72.552597   \n",
              "std       10.134247         11.126417         6.066053          10.274834   \n",
              "min        0.000000       -748.016667       -74.015515         -75.350437   \n",
              "25%        6.000000        -73.992072        40.734928         -73.991518   \n",
              "50%        8.500000        -73.981850        40.752453         -73.980205   \n",
              "75%       12.900000        -73.967331        40.767127         -73.963435   \n",
              "max      350.000000         40.770667        45.031653          40.828377   \n",
              "\n",
              "       dropoff_latitude  passenger_count  \n",
              "count      26781.000000     26781.000000  \n",
              "mean          39.942666         1.674695  \n",
              "std            6.061108         1.294758  \n",
              "min          -74.008745         0.000000  \n",
              "25%           40.733802         1.000000  \n",
              "50%           40.752927         1.000000  \n",
              "75%           40.768173         2.000000  \n",
              "max           45.031598         6.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c868842e-cc32-4f92-b117-b826bf6aa046\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fare_amount</th>\n",
              "      <th>pickup_longitude</th>\n",
              "      <th>pickup_latitude</th>\n",
              "      <th>dropoff_longitude</th>\n",
              "      <th>dropoff_latitude</th>\n",
              "      <th>passenger_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>26781.000000</td>\n",
              "      <td>26781.000000</td>\n",
              "      <td>26781.000000</td>\n",
              "      <td>26781.000000</td>\n",
              "      <td>26781.000000</td>\n",
              "      <td>26781.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>11.409123</td>\n",
              "      <td>-72.562169</td>\n",
              "      <td>39.940917</td>\n",
              "      <td>-72.552597</td>\n",
              "      <td>39.942666</td>\n",
              "      <td>1.674695</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>10.134247</td>\n",
              "      <td>11.126417</td>\n",
              "      <td>6.066053</td>\n",
              "      <td>10.274834</td>\n",
              "      <td>6.061108</td>\n",
              "      <td>1.294758</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>-748.016667</td>\n",
              "      <td>-74.015515</td>\n",
              "      <td>-75.350437</td>\n",
              "      <td>-74.008745</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>6.000000</td>\n",
              "      <td>-73.992072</td>\n",
              "      <td>40.734928</td>\n",
              "      <td>-73.991518</td>\n",
              "      <td>40.733802</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>8.500000</td>\n",
              "      <td>-73.981850</td>\n",
              "      <td>40.752453</td>\n",
              "      <td>-73.980205</td>\n",
              "      <td>40.752927</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>12.900000</td>\n",
              "      <td>-73.967331</td>\n",
              "      <td>40.767127</td>\n",
              "      <td>-73.963435</td>\n",
              "      <td>40.768173</td>\n",
              "      <td>2.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>350.000000</td>\n",
              "      <td>40.770667</td>\n",
              "      <td>45.031653</td>\n",
              "      <td>40.828377</td>\n",
              "      <td>45.031598</td>\n",
              "      <td>6.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c868842e-cc32-4f92-b117-b826bf6aa046')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c868842e-cc32-4f92-b117-b826bf6aa046 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c868842e-cc32-4f92-b117-b826bf6aa046');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Identify Outliers**"
      ],
      "metadata": {
        "id": "Yp1NRJeltxwQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# data visualization\n",
        "# plotting distribution plot\n",
        "\n",
        "sns.distplot(df['fare_amount'])\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "id": "6-aFnG2Xt05j",
        "outputId": "ecd20169-9b36-4e86-a231-868ee84f7457"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
            "  warnings.warn(msg, FutureWarning)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.distplot(df['pickup_latitude'])\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 337
        },
        "id": "yprfgqP7t7CH",
        "outputId": "6881e611-81b6-48c7-a69a-b614fc9377ed"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/seaborn/distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
            "  warnings.warn(msg, FutureWarning)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#creating a function to identify outliers\n",
        "\n",
        "def find_outliers(df):\n",
        "   q1 = df.quantile(0.25)\n",
        "   q3 = df.quantile(0.75)\n",
        "   IQR = q3-q1\n",
        "   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]\n",
        "   return outliers"
      ],
      "metadata": {
        "id": "F_4C8oZNuIpU"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#getting outlier details for column \"fair_amount\" using the above function\n",
        "\n",
        "outliers = find_outliers(df[\"fare_amount\"])\n",
        "print(\"number of outliers: \"+ str(len(outliers)))\n",
        "print(\"max outlier value: \"+ str(outliers.max()))\n",
        "print(\"min outlier value: \"+ str(outliers.min()))\n",
        "outliers"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4tVfJ59cuLqM",
        "outputId": "3a361388-cc2e-48e7-e14d-4804192ff41e"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "number of outliers: 2166\n",
            "max outlier value: 350.0\n",
            "min outlier value: 23.3\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6        24.5\n",
              "30       25.7\n",
              "34       39.5\n",
              "39       29.0\n",
              "48       56.8\n",
              "         ... \n",
              "26709    30.1\n",
              "26736    45.0\n",
              "26754    35.0\n",
              "26772    52.0\n",
              "26777    24.5\n",
              "Name: fare_amount, Length: 2166, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**3. Check the correlation**"
      ],
      "metadata": {
        "id": "pI9VFNbuuplm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#creating a correlation matrix\n",
        "\n",
        "corrMatrix = df.corr()\n",
        "sns.heatmap(corrMatrix, annot=True)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 347
        },
        "id": "wfmTXSlfuuje",
        "outputId": "fb66155a-f031-44ee-d15b-d4ec69a22d58"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "KFDp2Nvfu7ak",
        "outputId": "7648157c-f70a-4b2b-916a-85c1ec6020c8"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   fare_amount  pickup_longitude  pickup_latitude  dropoff_longitude  \\\n",
              "0          7.5        -73.999817        40.738354         -73.999512   \n",
              "1          7.7        -73.994355        40.728225         -73.994710   \n",
              "2         12.9        -74.005043        40.740770         -73.962565   \n",
              "3          5.3        -73.976124        40.790844         -73.965316   \n",
              "4         16.0        -73.925023        40.744085         -73.973082   \n",
              "\n",
              "   dropoff_latitude  passenger_count  \n",
              "0         40.723217              1.0  \n",
              "1         40.750325              1.0  \n",
              "2         40.772647              1.0  \n",
              "3         40.803349              3.0  \n",
              "4         40.761247              5.0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e6e573b1-97ae-4d41-b514-a402f489f676\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>fare_amount</th>\n",
              "      <th>pickup_longitude</th>\n",
              "      <th>pickup_latitude</th>\n",
              "      <th>dropoff_longitude</th>\n",
              "      <th>dropoff_latitude</th>\n",
              "      <th>passenger_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>7.5</td>\n",
              "      <td>-73.999817</td>\n",
              "      <td>40.738354</td>\n",
              "      <td>-73.999512</td>\n",
              "      <td>40.723217</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>7.7</td>\n",
              "      <td>-73.994355</td>\n",
              "      <td>40.728225</td>\n",
              "      <td>-73.994710</td>\n",
              "      <td>40.750325</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>12.9</td>\n",
              "      <td>-74.005043</td>\n",
              "      <td>40.740770</td>\n",
              "      <td>-73.962565</td>\n",
              "      <td>40.772647</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5.3</td>\n",
              "      <td>-73.976124</td>\n",
              "      <td>40.790844</td>\n",
              "      <td>-73.965316</td>\n",
              "      <td>40.803349</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>16.0</td>\n",
              "      <td>-73.925023</td>\n",
              "      <td>40.744085</td>\n",
              "      <td>-73.973082</td>\n",
              "      <td>40.761247</td>\n",
              "      <td>5.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e6e573b1-97ae-4d41-b514-a402f489f676')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e6e573b1-97ae-4d41-b514-a402f489f676 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e6e573b1-97ae-4d41-b514-a402f489f676');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5d0BXlo5u9ob",
        "outputId": "d1df1213-2da2-4a8a-bc49-cd9afdb7d9f9"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 26781 entries, 0 to 26780\n",
            "Data columns (total 6 columns):\n",
            " #   Column             Non-Null Count  Dtype  \n",
            "---  ------             --------------  -----  \n",
            " 0   fare_amount        26781 non-null  float64\n",
            " 1   pickup_longitude   26781 non-null  float64\n",
            " 2   pickup_latitude    26781 non-null  float64\n",
            " 3   dropoff_longitude  26781 non-null  float64\n",
            " 4   dropoff_latitude   26781 non-null  float64\n",
            " 5   passenger_count    26781 non-null  float64\n",
            "dtypes: float64(6)\n",
            "memory usage: 1.4 MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#splitting the data into train and test\n",
        "\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "rB0LgQkTvBrC"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#independent variables (x)\n",
        "\n",
        "x=df.drop(\"fare_amount\", axis=1)\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "gSWnvM_RvEvT",
        "outputId": "609ba989-113f-43c5-d683-8f5a813307f6"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  \\\n",
              "0            -73.999817        40.738354         -73.999512         40.723217   \n",
              "1            -73.994355        40.728225         -73.994710         40.750325   \n",
              "2            -74.005043        40.740770         -73.962565         40.772647   \n",
              "3            -73.976124        40.790844         -73.965316         40.803349   \n",
              "4            -73.925023        40.744085         -73.973082         40.761247   \n",
              "...                 ...              ...                ...               ...   \n",
              "26776        -73.987007        40.745440         -73.980320         40.748597   \n",
              "26777        -73.987893        40.744102         -73.981747         40.666842   \n",
              "26778        -73.992994        40.742853         -73.973609         40.738749   \n",
              "26779        -73.982207        40.770703         -74.003693         40.743873   \n",
              "26780        -73.989708        40.734386         -74.012733         40.704136   \n",
              "\n",
              "       passenger_count  \n",
              "0                  1.0  \n",
              "1                  1.0  \n",
              "2                  1.0  \n",
              "3                  3.0  \n",
              "4                  5.0  \n",
              "...                ...  \n",
              "26776              1.0  \n",
              "26777              1.0  \n",
              "26778              1.0  \n",
              "26779              5.0  \n",
              "26780              1.0  \n",
              "\n",
              "[26781 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bf92f5c0-32a3-424b-9aed-2b043991603b\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>pickup_longitude</th>\n",
              "      <th>pickup_latitude</th>\n",
              "      <th>dropoff_longitude</th>\n",
              "      <th>dropoff_latitude</th>\n",
              "      <th>passenger_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>-73.999817</td>\n",
              "      <td>40.738354</td>\n",
              "      <td>-73.999512</td>\n",
              "      <td>40.723217</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-73.994355</td>\n",
              "      <td>40.728225</td>\n",
              "      <td>-73.994710</td>\n",
              "      <td>40.750325</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>-74.005043</td>\n",
              "      <td>40.740770</td>\n",
              "      <td>-73.962565</td>\n",
              "      <td>40.772647</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>-73.976124</td>\n",
              "      <td>40.790844</td>\n",
              "      <td>-73.965316</td>\n",
              "      <td>40.803349</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>-73.925023</td>\n",
              "      <td>40.744085</td>\n",
              "      <td>-73.973082</td>\n",
              "      <td>40.761247</td>\n",
              "      <td>5.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26776</th>\n",
              "      <td>-73.987007</td>\n",
              "      <td>40.745440</td>\n",
              "      <td>-73.980320</td>\n",
              "      <td>40.748597</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26777</th>\n",
              "      <td>-73.987893</td>\n",
              "      <td>40.744102</td>\n",
              "      <td>-73.981747</td>\n",
              "      <td>40.666842</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26778</th>\n",
              "      <td>-73.992994</td>\n",
              "      <td>40.742853</td>\n",
              "      <td>-73.973609</td>\n",
              "      <td>40.738749</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26779</th>\n",
              "      <td>-73.982207</td>\n",
              "      <td>40.770703</td>\n",
              "      <td>-74.003693</td>\n",
              "      <td>40.743873</td>\n",
              "      <td>5.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26780</th>\n",
              "      <td>-73.989708</td>\n",
              "      <td>40.734386</td>\n",
              "      <td>-74.012733</td>\n",
              "      <td>40.704136</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>26781 rows × 5 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bf92f5c0-32a3-424b-9aed-2b043991603b')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-bf92f5c0-32a3-424b-9aed-2b043991603b button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-bf92f5c0-32a3-424b-9aed-2b043991603b');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#dependent variable (y)\n",
        "\n",
        "y=df[\"fare_amount\"]\n",
        "y"
      ],
      "metadata": {
        "id": "OFIibtb6vHso",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a6b361ea-276e-4bf2-8267-92111438fa07"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0         7.5\n",
              "1         7.7\n",
              "2        12.9\n",
              "3         5.3\n",
              "4        16.0\n",
              "         ... \n",
              "26776     4.5\n",
              "26777    24.5\n",
              "26778     6.5\n",
              "26779     8.9\n",
              "26780    12.5\n",
              "Name: fare_amount, Length: 26781, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)"
      ],
      "metadata": {
        "id": "JErN9_ievKuH"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. Implement linear regression and random forest regression models.\n",
        "5. Evaluate the models and compare their respective scores like R2, RMSE, etc."
      ],
      "metadata": {
        "id": "SDtRXJcAvs05"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Linear Regression\n",
        "\n",
        "from sklearn.linear_model import LinearRegression\n",
        "lrmodel=LinearRegression()\n",
        "lrmodel.fit(x_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WPNTcbDkvuf8",
        "outputId": "bd8acf10-1d9c-453e-ca1d-5fda6802a9ee"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "predictedvalues = lrmodel.predict(x_test)"
      ],
      "metadata": {
        "id": "qGkEYk9Tv12h"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Calculating the value of RMSE for Linear Regression\n",
        "\n",
        "from sklearn.metrics import mean_squared_error\n",
        "lrmodelrmse = np.sqrt(mean_squared_error(predictedvalues, y_test))\n",
        "print(\"RMSE value for Linear regression is\", lrmodelrmse)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZrloRtqCv4uK",
        "outputId": "6a77a3dd-f9db-4a49-cb2a-36c17ad2a593"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RMSE value for Linear regression is 9.98056567566619\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Random Forest Regression\n",
        "\n",
        "from sklearn.ensemble import RandomForestRegressor\n",
        "rfrmodel = RandomForestRegressor()"
      ],
      "metadata": {
        "id": "zffgQowjv757"
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rfrmodel.fit(x_train,y_train)\n",
        "rfrmodel_pred= rfrmodel.predict(x_test)"
      ],
      "metadata": {
        "id": "srgsFRXyv--v"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Calculating the value of RMSE for Random Forest Regression\n",
        "\n",
        "rfrmodel_rmse=np.sqrt(mean_squared_error(rfrmodel_pred, y_test))\n",
        "print(\"RMSE value for Random forest regression is \",rfrmodel_rmse)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EvzWKxOfwdHN",
        "outputId": "797ed45d-0a72-411c-b871-f42c531810d0"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RMSE value for Random forest regression is  5.015682452439671\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rfrmodel_pred.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EyHsbNbvwfvJ",
        "outputId": "224ce0e7-8d4a-4d65-a155-b99c9e198ce0"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5357,)"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    }
  ]
}
