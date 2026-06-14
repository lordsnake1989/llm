import streamlit as st

st.title("Chatbot de Atención al Cliente")

st.write("Bienvenido. Puedo ayudarte con pedidos, devoluciones, horarios, precios, promociones, pagos y envíos.")

pregunta = st.text_input("Escribe tu consulta:")

if pregunta:
    texto = pregunta.lower()

    if "pedido" in texto or "orden" in texto:
        respuesta = "Consultando base de datos de pedidos... Tu pedido está en preparación y llegará pronto."

    elif "devolucion" in texto or "reembolso" in texto:
        respuesta = "Puedes solicitar una devolución dentro de los primeros 7 días con tu ticket de compra."

    elif "horario" in texto or "abren" in texto or "cierran" in texto:
        respuesta = "Nuestro horario es de lunes a sábado de 9:00 AM a 7:00 PM."

    elif "precio" in texto or "costo" in texto or "vale" in texto:
        respuesta = "Los precios varían según el producto. Indícame cuál producto deseas consultar."

    elif "envio" in texto or "entrega" in texto:
        respuesta = "Sí realizamos envíos. El tiempo estimado depende de tu ubicación."

    elif "promocion" in texto or "descuento" in texto:
        respuesta = "Actualmente tenemos promociones activas en productos seleccionados."

    elif "pago" in texto or "tarjeta" in texto or "efectivo" in texto:
        respuesta = "Aceptamos efectivo, tarjetas de crédito y débito."

    elif "sucursal" in texto or "ubicacion" in texto:
        respuesta = "Tenemos sucursales en diferentes zonas. Indícame tu ciudad para ayudarte."

    elif "hola" in texto or "buenas" in texto:
        respuesta = "Hola, ¿en qué puedo ayudarte hoy?"

    else:
        respuesta = "Puedo ayudarte con pedidos, devoluciones, horarios, precios, promociones, pagos y envíos."

    st.subheader("Respuesta:")
    st.write(respuesta)