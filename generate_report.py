#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar el Informe Técnico Académico en PDF
Proyecto: Conversor de Unidades (Android - Jetpack Compose - MVVM)
Autor: Edgar Solis Hernandez
Universidad Politécnica de Chiapas
Grupo: 4B
Ingeniería en Tecnologías de la Información e Innovación Digital
Repositorio: https://github.com/lolxde121/Conversor-Unidades
"""

import os
import sys
from PIL import Image as PILImage

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether, HRFlowable, Preformatted, Image as RLImage
)
from reportlab.pdfgen import canvas

# Rutas clave
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF = os.path.join(BASE_DIR, "Informe_Conversor_Unidades_Edgar_Solis.pdf")
ICON_WEBP = os.path.join(BASE_DIR, "app/src/main/res/mipmap-xxhdpi/ic_launcher.webp")
SWAP_PNG = os.path.join(BASE_DIR, "app/src/main/res/drawable/intercambiar.png")
CONVERTED_ICON = "/tmp/up_conversor_icon.png"

# Convertir ícono webp a png si existe
if os.path.exists(ICON_WEBP):
    try:
        im = PILImage.open(ICON_WEBP)
        im.save(CONVERTED_ICON, "PNG")
    except Exception as e:
        print(f"Aviso al convertir icono: {e}")
        CONVERTED_ICON = None
else:
    CONVERTED_ICON = None

# Paleta de colores
NAVY_PRIMARY = colors.HexColor("#0F2C59")     # Azul marino UPChiapas
NAVY_SECONDARY = colors.HexColor("#1E4E8C")   # Azul medio
TEAL_ACCENT = colors.HexColor("#0284C7")      # Cyan tecnológico
DARK_TEXT = colors.HexColor("#1E293B")        # Gris texto principal
MUTED_TEXT = colors.HexColor("#475569")       # Gris texto secundario
LIGHT_BG = colors.HexColor("#F8FAFC")         # Fondo suave
CARD_BG = colors.HexColor("#F1F5F9")          # Fondo tarjetas
BORDER_COLOR = colors.HexColor("#CBD5E1")     # Bordes sutiles
CODE_BG = colors.HexColor("#0F172A")          # Fondo código oscuro
CODE_TEXT = colors.HexColor("#38BDF8")        # Color de código

class NumberedCanvas(canvas.Canvas):
    """
    Canvas de doble pasada para calcular 'Página X de Y'
    e imprimir encabezados y pies de página dinámicos.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        # Omitir portada
        if self._pageNumber == 1:
            return

        self.saveState()
        width, height = letter

        # Encabezado
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(NAVY_PRIMARY)
        self.drawString(45, height - 35, "UNIVERSIDAD POLITÉCNICA DE CHIAPAS")
        self.setFont("Helvetica", 8)
        self.setFillColor(MUTED_TEXT)
        self.drawString(225, height - 35, "|  ITIID - 4°B  |  Conversor de Unidades")

        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.75)
        self.line(45, height - 40, width - 45, height - 40)

        # Pie de página
        self.line(45, 42, width - 45, 42)

        self.setFont("Helvetica", 8)
        self.setFillColor(MUTED_TEXT)
        self.drawString(45, 30, "Edgar Solis Hernandez  •  GitHub: lolxde121/Conversor-Unidades")

        page_str = f"Página {self._pageNumber} de {total_pages}"
        self.drawRightString(width - 45, 30, page_str)

        self.restoreState()


def build_pdf():
    # Márgenes de 45pt izquierda/derecha, 50pt superior/inferior
    # Área imprimible horizontal: 612 - 90 = 522 pt
    # Área imprimible vertical: 792 - 100 = 692 pt
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_cover_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=NAVY_PRIMARY,
        alignment=1,
        spaceAfter=6
    )

    subtitle_cover_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=MUTED_TEXT,
        alignment=1,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=NAVY_PRIMARY,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=NAVY_SECONDARY,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=DARK_TEXT,
        spaceAfter=5,
        alignment=4
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3,
        alignment=4
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=NAVY_PRIMARY
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=DARK_TEXT
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.8,
        textColor=CODE_TEXT
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=DARK_TEXT
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=DARK_TEXT
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.white,
        alignment=1
    )

    story = []

    # =========================================================================
    # PÁGINA 1: PORTADA INSTITUCIONAL
    # =========================================================================
    story.append(Spacer(1, 10))

    # Encabezado institucional
    header_univ = [
        [Paragraph("<font size='15' color='#0F2C59'><b>UNIVERSIDAD POLITÉCNICA DE CHIAPAS</b></font>", ParagraphStyle('HUniv', parent=styles['Normal'], alignment=1))],
        [Paragraph("<font size='9.5' color='#1E4E8C'><b>DIRECCIÓN DE INGENIERÍA EN TECNOLOGÍAS DE LA INFORMACIÓN E INNOVACIÓN DIGITAL</b></font>", ParagraphStyle('HFac', parent=styles['Normal'], alignment=1))],
        [Paragraph("<font size='8.5' color='#64748B'><i>\"Ciencia y Tecnología con Compromiso Humano\"  •  Suchiapa, Chiapas</i></font>", ParagraphStyle('HSlog', parent=styles['Normal'], alignment=1))]
    ]
    t_header = Table(header_univ, colWidths=[522])
    t_header.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_header)

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=NAVY_PRIMARY, spaceAfter=14, spaceBefore=0))

    # Si existe el ícono, centrarlo
    if CONVERTED_ICON and os.path.exists(CONVERTED_ICON):
        img_badge = RLImage(CONVERTED_ICON, width=54, height=54)
        t_icon = Table([[img_badge]], colWidths=[522])
        t_icon.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
        story.append(t_icon)
        story.append(Spacer(1, 6))

    # Título principal del reporte
    story.append(Paragraph("REPORTE TÉCNICO DE PROYECTO", ParagraphStyle('RRep', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=TEAL_ACCENT, alignment=1, spaceAfter=5)))
    story.append(Paragraph("APLICACIÓN MÓVIL: CONVERSOR DE UNIDADES", title_cover_style))
    story.append(Paragraph("Desarrollo Android Nativo con Jetpack Compose, Arquitectura MVVM y StateFlow Reactivo", subtitle_cover_style))

    story.append(Spacer(1, 8))

    # Tarjeta de Datos del Alumno y del Proyecto
    meta_data = [
        [Paragraph("<b>Estudiante:</b>", meta_label), Paragraph("Edgar Solis Hernandez", meta_val)],
        [Paragraph("<b>Carrera / Programa:</b>", meta_label), Paragraph("Ingeniería en Tecnologías de la Información e Innovación Digital", meta_val)],
        [Paragraph("<b>Institución:</b>", meta_label), Paragraph("Universidad Politécnica de Chiapas (UPChiapas)", meta_val)],
        [Paragraph("<b>Grado y Grupo:</b>", meta_label), Paragraph("4° Cuatrimestre — Grupo 4B", meta_val)],
        [Paragraph("<b>Asignatura:</b>", meta_label), Paragraph("Programación y Desarrollo de Aplicaciones Móviles", meta_val)],
        [Paragraph("<b>Repositorio Oficial:</b>", meta_label), Paragraph('<link href="https://github.com/lolxde121/Conversor-Unidades" color="#0284C7"><u>https://github.com/lolxde121/Conversor-Unidades</u></link>', meta_val)],
        [Paragraph("<b>Fecha de Elaboración:</b>", meta_label), Paragraph("Octubre de 2026", meta_val)],
        [Paragraph("<b>Entorno Tecnológico:</b>", meta_label), Paragraph("Android SDK 37 (minSdk 30) | Kotlin 2.0+ | Material Design 3", meta_val)]
    ]

    t_meta = Table(meta_data, colWidths=[140, 360])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1.5, NAVY_PRIMARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_meta)

    story.append(Spacer(1, 14))

    # Síntesis ejecutiva en portada
    resumen_box = [
        [Paragraph("<b>SÍNTESIS DEL PROYECTO</b>", ParagraphStyle('RSin', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, textColor=NAVY_PRIMARY, alignment=1))],
        [Paragraph(
            "El presente informe documenta en detalle el diseño, arquitectura, formulación matemática y desarrollo de la aplicación móvil "
            "<b>Conversor de Unidades</b>, desarrollada por el estudiante <b>Edgar Solis Hernandez</b> del <b>Grupo 4B</b> en la "
            "<b>Universidad Politécnica de Chiapas</b>. La aplicación implementa el paradigma declarativo moderno en Android mediante "
            "<b>Jetpack Compose</b> y <b>Material 3</b>, estructurado bajo el patrón arquitectónico <b>MVVM (Model-View-ViewModel)</b> "
            "con sincronización bidireccional reactiva impulsada por <b>StateFlow</b> y corrutinas de Kotlin. Se incluye el enlace al "
            "código fuente abierto en GitHub: <font color='#0284C7'><b>https://github.com/lolxde121/Conversor-Unidades</b></font>.",
            body_style
        )]
    ]
    t_resumen = Table(resumen_box, colWidths=[522])
    t_resumen.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, TEAL_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_resumen)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 2: INTRODUCCIÓN, OBJETIVOS Y ARQUITECTURA MVVM
    # =========================================================================
    p2_content = []
    p2_content.append(Paragraph("1. Introducción y Justificación del Proyecto", h1_style))
    p2_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p2_content.append(Paragraph(
        "En la ingeniería moderna y en las actividades cotidianas, la conversión entre diferentes sistemas de medida "
        "(Sistema Internacional y Sistema Imperial) es una tarea fundamental que exige rapidez, precisión y una interfaz libre de fricción. "
        "Muchas herramientas móviles convencionales obligan al usuario a presionar botones manuales de 'Calcular' o reiniciar campos al alternar "
        "unidades de origen y destino. El proyecto <b>Conversor de Unidades</b> desarrollado por <b>Edgar Solis Hernandez</b> para la carrera de "
        "<b>Ingeniería en Tecnologías de la Información e Innovación Digital</b> en la <b>Universidad Politécnica de Chiapas</b> supera estas "
        "limitaciones implementando una experiencia <b>100% reactiva e instantánea</b>: cualquier cambio numérico o de unidad actualiza el "
        "resultado de forma transparente y en tiempo real.",
        body_style
    ))

    p2_content.append(Paragraph("1.1. Objetivos del Proyecto", h2_style))
    p2_content.append(Paragraph(
        "<b>Objetivo General:</b> Construir una aplicación móvil nativa en Android para la conversión precisa y bidireccional entre unidades "
        "de longitud (Centímetros, Metros, Kilómetros y Pulgadas), aplicando UI declarativa con Jetpack Compose y el patrón MVVM reactivo.",
        body_style
    ))
    p2_content.append(Paragraph("• <b>Modularidad:</b> Separar la presentación visual de la lógica de negocio mediante componentes desacoplados.", bullet_style))
    p2_content.append(Paragraph("• <b>Reactividad:</b> Utilizar <code>MutableStateFlow</code> y <code>StateFlow</code> para propagación inmediata de estados.", bullet_style))
    p2_content.append(Paragraph("• <b>Eficiencia Algorítmica:</b> Adoptar el metro como unidad pivote reduciendo la complejidad a O(N).", bullet_style))
    p2_content.append(Paragraph("• <b>Ergonomía UI/UX:</b> Crear una interfaz estilizada con superficies elevadas, selectores badge y contraste sobrio.", bullet_style))

    p2_content.append(Spacer(1, 4))
    p2_content.append(Paragraph("2. Arquitectura de Software y Patrón MVVM", h1_style))
    p2_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p2_content.append(Paragraph(
        "El proyecto implementa la arquitectura recomendada por Google: <b>Model-View-ViewModel (MVVM)</b>. "
        "Este patrón aísla el ciclo de vida de la actividad de los datos y asegura un código altamente testeable y mantenible.",
        body_style
    ))

    # Tabla descriptiva de capas arquitectónicas
    arq_data = [
        [Paragraph("<b>Capa</b>", table_header), Paragraph("<b>Componentes</b>", table_header), Paragraph("<b>Responsabilidad Principal</b>", table_header)],
        [
            Paragraph("<b>Vista (UI)</b>", table_cell_bold),
            Paragraph("<code>ConverseVMPage.kt</code><br/><code>TopBarrTitle.kt</code><br/><code>TitleUnit.kt</code>", table_cell),
            Paragraph("Renderizado declarativo con Jetpack Compose y Material 3. Captura eventos de usuario y recolecta estados mediante <code>collectAsStateWithLifecycle()</code>.", table_cell)
        ],
        [
            Paragraph("<b>ViewModel</b>", table_cell_bold),
            Paragraph("<code>ConverseUniViewModel.kt</code>", table_cell),
            Paragraph("Gestiona el estado reactivo mediante <code>StateFlow</code>. Procesa inputs de usuario, apertura/cierre de menús y coordina los recálculos.", table_cell)
        ],
        [
            Paragraph("<b>Modelo / Lógica</b>", table_cell_bold),
            Paragraph("Funciones <code>convertir()</code> y <code>formatearNumero()</code>", table_cell),
            Paragraph("Lógica pura de normalización matemática, factores escalares respecto al metro y formateo numérico localizado con 2 decimales.", table_cell)
        ]
    ]

    t_arq = Table(arq_data, colWidths=[80, 150, 292])
    t_arq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    p2_content.append(t_arq)

    p2_content.append(Spacer(1, 6))

    # Diagrama de flujo unidireccional
    flow_box = [
        [Paragraph(
            "<font color='#0F2C59'><b>[ VISTA (Jetpack Compose) ]</b></font>  "
            "───<i>(Evento: onInputChanged / seleccionarUnidad)</i>───►  "
            "<font color='#0F2C59'><b>[ VIEWMODEL (ConverseUniViewModel) ]</b></font><br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;▲&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;└───<i>(StateFlow actualizado: Recomposición de UI)</i>─── "
            "<font color='#0284C7'><b>[ LÓGICA DE CONVERSIÓN PIVOTE ]</b></font> ◄─┘",
            ParagraphStyle('FlowText', parent=styles['Normal'], fontName='Courier', fontSize=7.5, leading=11, alignment=1)
        )]
    ]
    t_flow = Table(flow_box, colWidths=[522])
    t_flow.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, NAVY_SECONDARY),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    p2_content.append(t_flow)

    story.append(KeepTogether(p2_content))
    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 3: MODELO MATEMÁTICO Y STACK TECNOLÓGICO
    # =========================================================================
    p3_content = []
    p3_content.append(Paragraph("3. Modelo Matemático y Lógica de Conversión", h1_style))
    p3_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p3_content.append(Paragraph(
        "Si se programaran conversiones directas entre cada par posible de unidades (ej. cm a m, cm a in, in a km, etc.), "
        "el número de combinaciones crecería de forma cuadrática: <i>K = N × (N - 1)</i>. Para 4 unidades se requerirían 12 casos condicionales, "
        "y para 10 unidades se requerirían 90 ramas de código, multiplicando el riesgo de errores aritméticos.",
        body_style
    ))
    p3_content.append(Paragraph(
        "<b>La técnica de la Unidad Pivote (Metro):</b> El software implementa el <b>Metro (m)</b> como unidad canónica de referencia. "
        "Cualquier magnitud de entrada se transforma primero a metros multiplicándola por su factor de escala, y posteriormente se divide "
        "entre el factor de la unidad destino. Esto reduce la complejidad a <b>O(N)</b>, logrando una arquitectura limpia y extensible.",
        body_style
    ))

    # Tabla de factores de conversión
    factors_data = [
        [Paragraph("<b>Unidad de Longitud</b>", table_header), Paragraph("<b>Símbolo</b>", table_header), Paragraph("<b>Factor a Metros (Escalar k)</b>", table_header), Paragraph("<b>Ecuación Canónica</b>", table_header)],
        [
            Paragraph("<b>Centímetro</b>", table_cell_bold),
            Paragraph("cm", table_cell),
            Paragraph("0.01", table_cell),
            Paragraph("<code>metros = valor × 0.01</code>", table_cell)
        ],
        [
            Paragraph("<b>Metro (Pivote Base)</b>", table_cell_bold),
            Paragraph("m", table_cell),
            Paragraph("1.0", table_cell),
            Paragraph("<code>metros = valor × 1.0</code>", table_cell)
        ],
        [
            Paragraph("<b>Kilómetro</b>", table_cell_bold),
            Paragraph("km", table_cell),
            Paragraph("1000.0", table_cell),
            Paragraph("<code>metros = valor × 1000.0</code>", table_cell)
        ],
        [
            Paragraph("<b>Pulgada (Imperial)</b>", table_cell_bold),
            Paragraph("in", table_cell),
            Paragraph("0.0254", table_cell),
            Paragraph("<code>metros = valor × 0.0254</code>", table_cell)
        ]
    ]

    t_factors = Table(factors_data, colWidths=[120, 60, 140, 202])
    t_factors.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    p3_content.append(t_factors)

    p3_content.append(Paragraph("3.1. Algoritmo Bidireccional y Formateo Inteligente", h2_style))
    p3_content.append(Paragraph(
        "Para evitar bucles de actualización infinita, las funciones <code>recalcularDesdeInput1</code> y <code>recalcularDesdeInput2</code> "
        "operan de forma asimétrica sobre el campo opuesto. Además, la función <code>formatearNumero</code> detecta si el resultado carece "
        "de parte decimal mediante <code>valor % 1.0f == 0.0f</code> (mostrando enteros limpios como '100' en vez de '100.00'), "
        "o aplica formato con dos decimales precisos (<code>Locale.US, \"%.2f\"</code>) en caso de números fraccionarios.",
        body_style
    ))

    p3_content.append(Spacer(1, 4))
    p3_content.append(Paragraph("4. Especificaciones Técnicas y Stack Tecnológico", h1_style))
    p3_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    stack_data = [
        [Paragraph("<b>Componente</b>", table_header), Paragraph("<b>Versión / Especificación</b>", table_header), Paragraph("<b>Justificación y Rol en el Proyecto</b>", table_header)],
        [
            Paragraph("<b>Lenguaje</b>", table_cell_bold),
            Paragraph("Kotlin 2.0+ (JVM 11)", table_cell),
            Paragraph("Código conciso, seguro ante nulos, con soporte de primera clase para corrutinas y sintaxis reactiva.", table_cell)
        ],
        [
            Paragraph("<b>UI Toolkit</b>", table_cell_bold),
            Paragraph("Jetpack Compose (BOM)", table_cell),
            Paragraph("Paradigma declarativo moderno que reemplaza XML, reduciendo boilerplate y optimizando recomposición.", table_cell)
        ],
        [
            Paragraph("<b>Sistema Visual</b>", table_cell_bold),
            Paragraph("Material Design 3 (M3)", table_cell),
            Paragraph("Estándar actual de Google con elevación de superficies, bordes suaves y contraste refinado.", table_cell)
        ],
        [
            Paragraph("<b>Gestión de Estado</b>", table_cell_bold),
            Paragraph("StateFlow & ViewModel", table_cell),
            Paragraph("<code>lifecycle-viewmodel-compose</code> con <code>collectAsStateWithLifecycle</code> para consumo seguro del ciclo de vida.", table_cell)
        ],
        [
            Paragraph("<b>Android SDK</b>", table_cell_bold),
            Paragraph("minSdk: 30 | targetSdk: 37<br/>compileSdk: 37", table_cell),
            Paragraph("Compatibilidad garantizada desde Android 11 (R) hasta la versión más reciente (Android 15+).", table_cell)
        ],
        [
            Paragraph("<b>Build System</b>", table_cell_bold),
            Paragraph("Gradle con Kotlin DSL (*.kts)", table_cell),
            Paragraph("Scripts tipados con verificación de dependencias y autocompletado en compilación.", table_cell)
        ]
    ]

    t_stack = Table(stack_data, colWidths=[95, 145, 282])
    t_stack.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    p3_content.append(t_stack)

    story.append(KeepTogether(p3_content))
    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 4: COMPONENTES UI Y ANÁLISIS DE CÓDIGO FUENTE
    # =========================================================================
    p4_content = []
    p4_content.append(Paragraph("5. Diseño de Interfaz de Usuario y Componentes (UI/UX)", h1_style))
    p4_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p4_content.append(Paragraph(
        "La interfaz destaca por un diseño estilizado, ergonómico y minimalista compuesto por los siguientes módulos:",
        body_style
    ))

    comp_items = [
        ("TopBarTitle.kt", "Barra superior cilíndrica (RoundedCornerShape de 200.dp) con fondo gris claro (#D9D9D9), sombra de 4dp y tipografía centrada de 27.sp."),
        ("TitleUnit.kt", "Insignia táctil con fondo negro, bordes redondeados (9.dp) y texto blanco nítido que despliega el menú contextual al pulsarse."),
        ("DropdownMenu Dinámico", "Menú emergente con la lista de magnitudes (Centímetros, Metros, Kilómetros, Pulgadas) para selección ágil."),
        ("Surface de Entrada Numérica", "Contenedores de 314x119 dp con esquinas redondeadas de 45.dp, marco BorderStroke de 16.dp en color LightGray y sombra táctil."),
        ("BasicTextField Personalizado", "Campo configurado con KeyboardOptions(keyboardType = KeyboardType.Number), texto blanco centrado de 27.sp."),
        ("Ícono Central de Intercambio", "Recurso gráfico drawable (intercambiar.png) ubicado entre ambos campos, comunicando visualmente la sincronía bidireccional.")
    ]

    for c_title, c_desc in comp_items:
        p4_content.append(Paragraph(f"• <b>{c_title}:</b> {c_desc}", bullet_style))

    p4_content.append(Spacer(1, 4))
    p4_content.append(Paragraph("6. Análisis de Código Fuente y Buenas Prácticas", h1_style))
    p4_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p4_content.append(Paragraph(
        "A continuación se presenta el núcleo reactivo implementado en <code>ConverseUniViewModel.kt</code>:",
        body_style
    ))

    code_lines = [
        "// Estados reactivos encapsulados (MutableStateFlow privado / StateFlow público)",
        "private val _unidad1 = MutableStateFlow(\"Centímetros\")",
        "val unidad1: StateFlow<String> = _unidad1.asStateFlow()",
        "",
        "private val _inputText1 = MutableStateFlow(\"100\")",
        "val inputText1: StateFlow<String> = _inputText1.asStateFlow()",
        "",
        "// Lógica de conversión normalizada mediante unidad pivote (Metro)",
        "private fun convertir(valor: Float, deUnidad: String, aUnidad: String): Float {",
        "    val metros = when (deUnidad) {",
        "        \"Centímetros\" -> valor * 0.01f",
        "        \"Metros\"      -> valor * 1.0f",
        "        \"Kilómetros\"  -> valor * 1000.0f",
        "        \"Pulgadas\"    -> valor * 0.0254f",
        "        else          -> valor",
        "    }",
        "    return when (aUnidad) {",
        "        \"Centímetros\" -> metros / 0.01f",
        "        \"Metros\"      -> metros / 1.0f",
        "        \"Kilómetros\"  -> metros / 1000.0f",
        "        \"Pulgadas\"    -> metros / 0.0254f",
        "        else          -> metros",
        "    }",
        "}",
        "",
        "private fun recalcularDesdeInput1(texto: String) {",
        "    val valor = texto.toFloatOrNull() ?: run { _inputText2.value = \"\"; return }",
        "    val resultado = convertir(valor, _unidad1.value, _unidad2.value)",
        "    _inputText2.value = formatearNumero(resultado)",
        "}"
    ]

    p_code = Preformatted("\n".join(code_lines), code_style)
    t_code = Table([[p_code]], colWidths=[522])
    t_code.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CODE_BG),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#334155")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    p4_content.append(t_code)

    p4_content.append(Spacer(1, 4))
    p4_content.append(Paragraph(
        "<b>Puntos de Ingeniería Relevantes:</b><br/>"
        "1. <b>Encapsulamiento del Estado:</b> <code>_inputText1</code> y <code>_unidad1</code> son mutables privados, previniendo alteraciones no autorizadas fuera del ViewModel.<br/>"
        "2. <b>Resiliencia con <code>toFloatOrNull()</code>:</b> Si el usuario borra la entrada o introduce caracteres especiales, el sistema limpia el campo complementario de forma segura en lugar de lanzar una excepción <code>NumberFormatException</code>.",
        body_style
    ))

    story.append(KeepTogether(p4_content))
    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 5: CONTROL DE VERSIONES, CONCLUSIONES Y REFERENCIAS
    # =========================================================================
    p5_content = []
    p5_content.append(Paragraph("7. Control de Versiones y Repositorio en GitHub", h1_style))
    p5_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p5_content.append(Paragraph(
        "El desarrollo del proyecto fue gestionado rigurosamente mediante Git y alojado públicamente en GitHub: "
        '<link href="https://github.com/lolxde121/Conversor-Unidades" color="#0284C7"><b><u>https://github.com/lolxde121/Conversor-Unidades</u></b></link>. '
        "El historial evidencia una evolución incremental y estructurada:",
        body_style
    ))

    # Historial de commits
    commits_data = [
        [Paragraph("<b>Hash</b>", table_header), Paragraph("<b>Mensaje del Commit</b>", table_header), Paragraph("<b>Fase del Desarrollo</b>", table_header)],
        [Paragraph("<code>433bf97</code>", table_cell), Paragraph("primer:avance", table_cell), Paragraph("Configuración inicial Gradle y estructura del proyecto", table_cell)],
        [Paragraph("<code>4665ae4</code>", table_cell), Paragraph("componente: topBar Personalzado", table_cell), Paragraph("Diseño del componente TopBarTitle modular", table_cell)],
        [Paragraph("<code>2cb4369</code>", table_cell), Paragraph("primer version de componentes", table_cell), Paragraph("Creación inicial de componentes Compose", table_cell)],
        [Paragraph("<code>da5526f</code>", table_cell), Paragraph("primer version de componentes", table_cell), Paragraph("Refinamiento de parámetros en botones y campos", table_cell)],
        [Paragraph("<code>5db4dba</code>", table_cell), Paragraph("contenido inicial", table_cell), Paragraph("Vinculación de la pantalla principal en MainActivity", table_cell)],
        [Paragraph("<code>8ff1573</code>", table_cell), Paragraph("campos de texto, menu desplegable", table_cell), Paragraph("Integración de BasicTextField y DropdownMenu", table_cell)],
        [Paragraph("<code>f552762</code>", table_cell), Paragraph("primera version conversion", table_cell), Paragraph("Lógica matemática y sincronización con ViewModel", table_cell)],
        [Paragraph("<code>684ac12</code>", table_cell), Paragraph("fix: ajuste en campo ahora se vee meor la unidad dentro del campo negro", table_cell), Paragraph("Ajuste visual y padding de texto en TitleUnit", table_cell)]
    ]

    t_commits = Table(commits_data, colWidths=[65, 235, 222])
    t_commits.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    p5_content.append(t_commits)

    p5_content.append(Spacer(1, 4))
    p5_content.append(Paragraph("8. Conclusiones y Trabajo Futuro", h1_style))
    p5_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    p5_content.append(Paragraph(
        "<b>Conclusiones del Proyecto:</b><br/>"
        "• <b>Eficiencia con Jetpack Compose:</b> La eliminación del XML redujo notablemente las líneas de código y facilitó un diseño reactivo y adaptativo.<br/>"
        "• <b>Robustez del Patrón MVVM:</b> Concentrar la lógica y los estados en el ViewModel garantiza que la interfaz siempre refleje el estado real de la aplicación.<br/>"
        "• <b>Escalabilidad:</b> La metodología de unidad pivote (metro) permite incorporar nuevas unidades de longitud con una sola línea de código adicional.<br/>"
        "• <b>Desarrollo Académico:</b> El proyecto consolida las competencias de programación móvil del alumno <b>Edgar Solis Hernandez</b> en la <b>UPChiapas</b>.",
        body_style
    ))
    p5_content.append(Paragraph(
        "<b>Líneas de Trabajo Futuro:</b><br/>"
        "• <b>Nuevas Categorías:</b> Incorporar pestañas para magnitudes de Masa (kg, lb), Temperatura (°C, °F, K) y Velocidad (km/h, mph).<br/>"
        "• <b>Persistencia Local:</b> Integrar Room Database para almacenar el historial de conversiones recientes.<br/>"
        "• <b>Internacionalización:</b> Soporte multilenguaje (inglés/español) y temas claros/oscuros adaptativos.",
        body_style
    ))

    p5_content.append(Spacer(1, 4))
    p5_content.append(Paragraph("9. Referencias y Enlaces Oficiales", h1_style))
    p5_content.append(HRFlowable(width="100%", thickness=1, color=NAVY_SECONDARY, spaceAfter=6, spaceBefore=0))

    ref_items = [
        ("Repositorio GitHub del Proyecto", "https://github.com/lolxde121/Conversor-Unidades", "Código fuente, commits e historial de versiones por Edgar Solis."),
        ("Guía de Arquitectura de Apps Android", "https://developer.android.com/topic/architecture", "Patrones y recomendaciones oficiales de Google Developers."),
        ("Documentación de Jetpack Compose", "https://developer.android.com/jetpack/compose", "Guías oficiales del toolkit moderno de interfaz declarativa."),
        ("Kotlin Coroutines y StateFlow", "https://kotlinlang.org/docs/flow.html", "Documentación oficial de Kotlin para flujos reactivos asíncronos.")
    ]

    for r_title, r_url, r_desc in ref_items:
        p5_content.append(Paragraph(
            f"• <b>{r_title}:</b> <link href='{r_url}' color='#0284C7'><u>{r_url}</u></link> — <i>{r_desc}</i>",
            bullet_style
        ))

    story.append(KeepTogether(p5_content))

    # Construir documento
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Informe generado exitosamente en: {OUTPUT_PDF}")

if __name__ == "__main__":
    build_pdf()
