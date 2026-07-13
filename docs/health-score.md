# ¿Cómo sabemos si un cliente está sano?


### Ponderamos el impacto de cada KPI:


KPI              |Type   | Value| Impacto | 
--------------------------------------------
Último login     |días   |  3   | ALTO    |
NPS              |score  | 10   | ALTO    |
Tickets abiertos |ticket |  0   | MEDIO   |
Usuarios activos |team   | 14   | MEDIO   | 

### Ideal:

últimoLogin = 0 días : OK
NPS >= 8 : OK
ticketsAbiertos <= 2: OK
usuariosActivos > 11 : OK



### Al contrario, si:

últimoLogin < 2 días : WARN
NPS <= 7: WARN
ticketsAbiertos < 10 : WARN
usuariosActivos < 10 : WARN


La idea es poder cubrir los principales KPIs disponibles y exprimirlos al máximo: *NPS* y *últimoLogin* son clave para entender el comportamiento diario del cliente, mientras que *ticketsAbiertos* y *usuariosActivos* son más **coyunturales** y **situacionales**. 

