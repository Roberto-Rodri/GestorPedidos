import pandas as pd
import random

# --- Nombres de clientes y productos ---
nombres_clientes = [
    "Juan García", "María Rodríguez", "José Martínez", "Carmen Hernández", "Francisco López",
    "Ana González", "Manuel Pérez", "Isabel Sánchez", "Pedro Ramírez", "Rosa Cruz",
    "Miguel Gómez", "Dolores Flores", "Ángel Morales", "Josefa Vázquez", "Carlos Jiménez",
    "Teresa Reyes", "Alejandro Díaz", "Guadalupe Torres", "Roberto Gutiérrez", "Antonia Ruiz",
    "Fernando Mendoza", "Francisca Aguilar", "Daniel Méndez", "Marta Castillo", "Jorge Ortiz",
    "Elena Moreno", "Ricardo Rivera", "Mercedes Ramos", "Eduardo Romero", "Pilar Juárez",
    "Javier Álvarez", "Victoria Castillo", "Raúl Chávez", "Juana Soto", "Víctor Vargas",
    "Cecilia Luna", "Sergio Ortega", "Esther Medina", "Luis Delgado", "Yolanda Vega",
    "Alberto Rojas", "Gloria Silva", "Gabriel Márquez", "Alicia Navarro", "Rogelio Salazar",
    "Silvia Castro", "Arturo Pineda", "Beatriz Fuentes", "Gerardo Guzmán", "Leticia Valadez",
    "Hugo Gallegos", "Verónica Méndez", "Leonardo Pacheco", "Irene Miranda", "Guillermo Rangel",
    "Blanca Trejo", "Felipe Islas", "Sandra Valencia", "Ignacio Guerrero", "Olga Herrera",
    "Mario Medina", "Adriana Esquivel", "Alfonso Benítez", "Julia Cabrera", "Salvador Acosta",
    "Lorena Meza", "Enrique Santillán", "Guillermina Villalobos", "Marcos Rosas", "Mónica Espinoza",
    "Ramón Padilla", "Lourdes Calderón", "Francisco Tapia", "Araceli Zúñiga", "Oscar Peralta",
    "Socorro Arellano", "Héctor Cervantes", "Claudia Beltrán", "Alfredo Corona", "Raquel Sotelo",
    "Fabián Aguirre", "Graciela Bernal", "Mauricio Orozco", "Luisa Montaño", "Joaquín Parra",
    "Rosario Galván", "Matías Mares", "Angélica Montes", "Simón Cárdenas", "Patricia Leyva",
    "Tomás Valenzuela", "Imelda Trujillo", "Agustín Macías", "Alejandra Mares", "Gregorio Saucedo",
    "Amalia Tovar", "Esteban Jurado", "Rebeca Granados", "Fermín Barajas", "Sonia Becerra"
]

nombres_productos = [
    "Arroz Extra (1kg)", "Frijol Negro (1kg)", "Aceite Vegetal (1L)", "Leche Entera (1L)",
    "Huevo Blanco (18 piezas)", "Azúcar Estándar (1kg)", "Sal de Mesa (1kg)", "Harina de Trigo (1kg)",
    "Pasta para Sopa (200g)", "Atún en Agua (140g)", "Mayonesa (390g)", "Salsa de Tomate (210g)",
    "Café Soluble (190g)", "Cereal de Maíz (500g)", "Galletas Marías (170g)", "Pan de Caja Blanco",
    "Tortillas de Harina (10 pzas)", "Refresco de Cola (600ml)", "Agua Mineral (600ml)", "Jugo de Naranja (1L)",
    "Papas Fritas Saladas", "Chicharrones de Cerdo", "Chocolate en Polvo (400g)", "Mermelada de Fresa",
    "Chiles Jalapeños en Vinagre", "Queso Panela (400g)", "Jamón de Pavo (250g)", "Yogurt para Beber",
    "Detergente en Polvo (900g)", "Jabón de Trastes Líquido", "Suavizante de Telas (1L)", "Limpiador de Pisos (1L)",
    "Cloro (1L)", "Jabón de Tocador", "Papel Higiénico (4 rollos)", "Pasta de Dientes",
    "Shampoo (750ml)", "Servilletas (100 piezas)", "Esponja para Trastes", "Encendedor de Cocina"
]

# --- Estados de los pedidos ---

estados = [
    "pagado", "pendiente", "cancelado"
]

pedidos = {}

# --- Generacion de pedidos de manera aleatoria ---

for i in range(1, 21):
    pedidos[i] = {
        "cliente": random.choice(nombres_clientes),
        "producto": random.choice(nombres_productos),
        "cantidad": random.randint(1,5),
        "estado": random.choice(estados)
    }

# --- Convertir a DataFrame pedidos ---
df_pedidos = pd.DataFrame.from_dict(pedidos, orient="index")