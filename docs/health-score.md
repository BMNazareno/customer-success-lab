# Health Score

## ¿Cómo sabemos si un cliente está sano?

Para evaluar la salud de un cliente, ponderamos el impacto de cada KPI según su relevancia para el seguimiento diario y la evolución del negocio.

### KPIs considerados

| KPI | Tipo | Valor | Impacto |
| --- | --- | ---: | --- |
| Último login | días | 3 | Alto |
| NPS | score | 10 | Alto |
| Tickets abiertos | ticket | 0 | Medio |
| Usuarios activos | team | 14 | Medio |

### Condiciones ideales

- Último login = 0 días: OK
- NPS >= 8: OK
- Tickets abiertos <= 2: OK
- Usuarios activos > 11: OK

### Señales de alerta

- Último login < 2 días: WARN
- NPS <= 7: WARN
- Tickets abiertos < 10: WARN
- Usuarios activos < 10: WARN

### Nota de interpretación

La idea es cubrir los principales KPIs disponibles y aprovecharlos al máximo. *NPS* y *último login* resultan clave para entender el comportamiento diario del cliente, mientras que *tickets abiertos* y *usuarios activos* son más *coyunturales* y *situacionales*.

