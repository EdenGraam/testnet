{\rtf1\ansi\ansicpg1251\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 WITH\
  testnet AS (\
    SELECT\
      SUM(value / 1e18) AS total,\
      "from"\
    FROM\
      ethereum."transactions"\
    WHERE\
      "to" = '\\x0a9f824c05a74f577a536a8a0c673183a872dff4' -- testnet LayerZero bridge\
      AND value > 0\
      AND success\
    GROUP BY\
      "from"\
  )\
SELECT\
  COUNT(DISTINCT testnet."from") AS users,\
  CASE\
    WHEN testnet.total < 0.01 THEN '< 0.01 ETH'\
    WHEN testnet.total BETWEEN 0.01 AND 0.1 THEN '0.01 ~ 0.1 ETH'\
    WHEN testnet.total BETWEEN 0.1 AND 1 THEN '0.1 ~ 1 ETH'\
    WHEN testnet.total BETWEEN 1 AND 5 THEN '1 ~ 5 ETH'\
    WHEN testnet.total BETWEEN 5 AND 10 THEN '5 ~ 10 ETH'\
    WHEN testnet.total BETWEEN 10 AND 20 THEN '10 ~ 20 ETH'\
    ELSE '> 20 ETH'\
  END AS "eth_value_gap"\
FROM testnet\
GROUP BY 2  }