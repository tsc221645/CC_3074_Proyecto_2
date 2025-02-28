# Modelos de Regresión Lineal

## Información de la Empresa

**InmoValor S.A.** es una empresa innovadora en el sector inmobiliario que utiliza técnicas avanzadas de análisis y modelos de regresión para estimar el valor de los inmuebles. La compañía recopila y analiza un amplio conjunto de datos con información detallada sobre viviendas, con el objetivo de desarrollar modelos predictivos que permitan proyectar con precisión el precio de los inmuebles.

Cada semana, se generan y entregan resultados basados en la aplicación de algoritmos de predicción y/o clasificación. El objetivo final es determinar el mejor algoritmo predictivo para estimar con mayor exactitud el valor de una vivienda.

## Información del DataSet

| Número | Nombre de la Columna | Significado | Tipo de Dato |
|--------|----------------------|-------------|-------------|
| 1 | MSSubClass | Clase del edificio | int64 |
| 2 | MSZoning | Clasificación de zonificación | object |
| 3 | LotFrontage | Pies lineales de calle conectados a la propiedad | float64 |
| 4 | LotArea | Tamaño del terreno en pies cuadrados | int64 |
| 5 | Street | Tipo de acceso a la calle | object |
| 6 | Alley | Tipo de acceso al callejón | object |
| 7 | LotShape | Forma general de la propiedad | object |
| 8 | LandContour | Nivelación del terreno | object |
| 9 | Utilities | Tipo de servicios disponibles | object |
| 10 | LotConfig | Configuración del terreno | object |
| 11 | LandSlope | Pendiente del terreno | object |
| 12 | Neighborhood | Ubicación dentro de los límites de Ames | object |
| 13 | Condition1 | Proximidad a carreteras o ferrocarriles | object |
| 14 | Condition2 | Proximidad a una segunda carretera o ferrocarril | object |
| 15 | BldgType | Tipo de vivienda | object |
| 16 | HouseStyle | Estilo de la vivienda | object |
| 17 | OverallQual | Calidad general de materiales y acabados | int64 |
| 18 | OverallCond | Calificación de la condición general | int64 |
| 19 | YearBuilt | Año de construcción original | int64 |
| 20 | YearRemodAdd | Año de remodelación | int64 |
| 21 | RoofStyle | Tipo de techo | object |
| 22 | RoofMatl | Material del techo | object |
| 23 | Exterior1st | Revestimiento exterior de la casa | object |
| 24 | Exterior2nd | Segundo revestimiento exterior (si aplica) | object |
| 25 | MasVnrType | Tipo de revestimiento de mampostería | object |
| 26 | MasVnrArea | Área de revestimiento de mampostería en pies cuadrados | float64 |
| 27 | ExterQual | Calidad del material exterior | object |
| 28 | ExterCond | Estado actual del material exterior | object |
| 29 | Foundation | Tipo de cimentación | object |
| 30 | BsmtQual | Altura del sótano | object |
| 31 | BsmtCond | Condición general del sótano | object |
| 32 | BsmtExposure | Exposición del sótano (nivel jardín o salida) | object |
| 33 | BsmtFinType1 | Calidad del área terminada del sótano | object |
| 34 | BsmtFinSF1 | Pies cuadrados de área terminada tipo 1 en el sótano | int64 |
| 35 | BsmtFinType2 | Calidad de la segunda área terminada del sótano | object |
| 36 | BsmtFinSF2 | Pies cuadrados de área terminada tipo 2 en el sótano | int64 |
| 37 | BsmtUnfSF | Pies cuadrados sin terminar del sótano | int64 |
| 38 | TotalBsmtSF | Pies cuadrados totales del sótano | int64 |
| 39 | Heating | Tipo de calefacción | object |
| 40 | HeatingQC | Calidad y condición de la calefacción | object |
| 41 | CentralAir | Aire acondicionado central | object |
| 42 | Electrical | Sistema eléctrico | object |
| 43 | 1stFlrSF | Pies cuadrados del primer piso | int64 |
| 44 | 2ndFlrSF | Pies cuadrados del segundo piso | int64 |
| 45 | LowQualFinSF | Pies cuadrados de acabado de baja calidad | int64 |
| 46 | GrLivArea | Pies cuadrados de área habitable sobre el suelo | int64 |
| 47 | BsmtFullBath | Número de baños completos en el sótano | int64 |
| 48 | BsmtHalfBath | Número de medios baños en el sótano | int64 |
| 49 | FullBath | Número de baños completos sobre el nivel del suelo | int64 |
| 50 | HalfBath | Número de medios baños sobre el nivel del suelo | int64 |
| 51 | BedroomAbvGr | Número de habitaciones sobre el sótano | int64 |
| 52 | KitchenAbvGr | Número de cocinas | int64 |
| 53 | KitchenQual | Calidad de la cocina | object |
| 54 | TotRmsAbvGrd | Total de habitaciones sobre el nivel del suelo (sin incluir baños) | int64 |
| 55 | Functional | Clasificación de funcionalidad de la casa | object |
| 56 | Fireplaces | Número de chimeneas | int64 |
| 57 | FireplaceQu | Calidad de la chimenea | object |
| 58 | GarageType | Ubicación del garaje | object |
| 59 | GarageYrBlt | Año de construcción del garaje | float64 |
| 60 | GarageFinish | Acabado interior del garaje | object |
| 61 | GarageCars | Tamaño del garaje en capacidad de autos | int64 |
| 62 | GarageArea | Tamaño del garaje en pies cuadrados | int64 |
| 63 | GarageQual | Calidad del garaje | object |
| 64 | GarageCond | Condición del garaje | object |
| 65 | PavedDrive | Entrada pavimentada | object |
| 66 | WoodDeckSF | Área de terraza de madera en pies cuadrados | int64 |
| 67 | OpenPorchSF | Área del porche abierto en pies cuadrados | int64 |
| 68 | EnclosedPorch | Área del porche cerrado en pies cuadrados | int64 |
| 69 | 3SsnPorch | Área del porche de tres estaciones en pies cuadrados | int64 |
| 70 | ScreenPorch | Área del porche con mosquitero en pies cuadrados | int64 |
| 71 | PoolArea | Área de la piscina en pies cuadrados | int64 |
| 72 | PoolQC | Calidad de la piscina | object |
| 73 | Fence | Calidad de la cerca | object |
| 74 | MiscFeature | Característica miscelánea no cubierta en otras categorías | object |
| 75 | MiscVal | Valor en dólares de la característica miscelánea | int64 |
| 76 | MoSold | Mes de venta | int64 |
| 77 | YrSold | Año de venta | int64 |
| 78 | SaleType | Tipo de venta | object |
| 79 | SaleCondition | Condición de venta | object |
| 80 | SalePrice | Precio de venta de la propiedad en dólares | int64 |

## Enlaces

- [**Información del DataSet**](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
