# DIY LC Meter Project

This project demonstrates how to build a DIY LC Meter capable of measuring inductance (L) and capacitance (C) values using an Arduino Nano, an LM311 comparator, and a 16x2 LCD display. The LC Meter is designed to be simple, affordable, and effective for electronics enthusiasts and DIY hobbyists. It is suitable for learning about measurement principles while also being a practical tool.

## Project Highlights:

### 1 - Circuit Schematic
A detailed circuit diagram explains the working principle and interconnection of components such as the LM311 comparator, relay, calibration buttons, and measurement probes. The schematic provides a foundation for assembling the hardware.

### 2 - PCB Design
A professionally designed single-layer PCB created with KiCad ensures clean routing and minimizes interference. It includes detailed silkscreen labels for easy assembly and debugging.

### 3 - 3D Model
A realistic 3D representation of the completed PCB with components mounted, offering a clear view of the final product and component placement.

### 4 - Firmware
The Arduino Nano is programmed with custom firmware to calculate inductance and capacitance values. Measurements are displayed on a 16x2 LCD in real time.

### 5 - Calibration and Functionality
The project includes functionality for calibration, zeroing, and easy measurement. Buttons on the PCB allow users to fine-tune settings for accurate results.

---

### Features:
- Precise Measurements: Measure a wide range of inductance and capacitance values.
- User-Friendly Interface: Includes a 16x2 LCD display for real-time measurement results and intuitive feedback.
- Adjustable Calibration: Easily calibrate the device for accurate readings using the on-board calibration buttons.
- Compact and Portable: The design is compact, making it easy to use in different workspaces or carry for fieldwork.


### Instructions:
### Prepare the PCB:
Download the provided Gerber files and manufacture the PCB, or use the KiCad design to etch your own board.

### Assemble Components:
Place and solder all components as per the silkscreen labels on the PCB.

### Upload Firmware:
Use the Arduino IDE to upload the provided sketch to your Arduino Nano. Ensure all libraries are correctly installed.

### Power and Calibration:
Connect the LC Meter to a 5V power source via USB or the provided input terminals. Calibrate the device using the calibration and zero buttons for precise results.

### Start Measuring:
Connect your inductors or capacitors to the respective terminals (Lx or Cx) and observe the measurement results on the LCD.

## Watch the Build Process

You can watch the full build process of this DIY LC Meter on my YouTube channel [**Teknotrek**](https://www.youtube.com/@TeknoTrek). Click the link below to see how the circuit is assembled, soldered, and tested:

[Watch on YouTube](https://youtu.be/YbbpxDlLRkQ)

## Files Included:
- Circuit schematic
- PCB design files (KiCad)
- 3D PCB model
- Arduino firmware
- Documentation with detailed assembly and usage instructions


## Circuit Schematic

![DIY LC Meter Schematic](https://raw.githubusercontent.com/TeknoTrek/LC-Meter/refs/heads/main/images/Circuit-LC-Meter.jpg)

## PCB Layout

![PCB Layout](https://raw.githubusercontent.com/TeknoTrek/LC-Meter/refs/heads/main/images/lc-meter-pcb-teknotrek.jpg)

## 3D Model

![3D Model](https://raw.githubusercontent.com/TeknoTrek/LC-Meter/refs/heads/main/images/lc-meter-treknotrek-pcb-3d-model-2.jpg)

![3D Model](https://raw.githubusercontent.com/TeknoTrek/LC-Meter/refs/heads/main/images/lc-meter-treknotrek-pcb-3d-model.jpg)

## GitHub Repository:
All project files, including schematics, PCB designs, 3D models, and source code, are available on GitHub.

Check out the project here: [**Teknotrek**](https://www.youtube.com/@TeknoTrek)

This project is perfect for anyone interested in electronics, DIY tools, or Arduino projects. Whether you are a beginner or an experienced maker,this LC Meter provides a hands-on learning experience and a functional tool for your electronics toolkit!

# Utilización de Arduino Mega 2560 R3.
Es totalmente posible adaptar este proyecto para utilizar un **Arduino Mega 2560 R3**. Basado en las librerías utilizadas, el soporte para el microcontrolador ATmega2560 ya está incluido, por lo que la adaptación consiste principalmente en cambios de cableado (hardware) y verificación de pines.

# Cambios de Hardware Requeridos

## 1. Entrada de Frecuencia (Librería FreqCount)
La librería `FreqCount` utiliza un temporizador de hardware específico para contar pulsos. Este pin cambia dependiendo de la placa utilizada.

    - **Arduino Nano:** Usa el **Pin 5** (Timer 1).
    - **Arduino Mega:** La librería define automáticamente el uso del **Pin 47** (Timer 5).

**Acción:** Debes conectar la señal de frecuencia (proveniente del comparador LM311) al **Pin 47** del Arduino Mega en lugar del Pin 5.

## 2. Pantalla LCD (I2C)
La comunicación I2C tiene pines dedicados diferentes en el Mega.

    - **Arduino Nano:** SDA es A4, SCL es A5.
    - **Arduino Mega:** SDA es el pin **20**, SCL es el pin **21**.

**Acción:** Conecta los pines SDA y SCL de tu pantalla LCD a los pines **20 y 21** del Arduino Mega respectivamente.

## 3. Otros Componentes (Relé y Botones)
El resto de los pines digitales (para el relé de calibración y los botones) deberían funcionar igual si utilizas los mismos números de pin definidos en el código original (por ejemplo, D2, D3, etc.), ya que el mapeo es directo en el entorno Arduino.

*Nota:* Al igual que en el Nano, la librería `FreqCount` utiliza el `TIMER2` para la ventana de tiempo. Esto significa que los pines **9 y 10** perderán su capacidad de PWM (`analogWrite`), pero pueden usarse como pines digitales normales.

# Resumen de Conexiones

lll@{}}

**Función**  |  **Arduino Nano**  |  **Arduino Mega 2560**   

Entrada Frecuencia  |  Pin 5  |  **Pin 47**   

LCD SDA  |  Pin A4  |  **Pin 20**   

LCD SCL  |  Pin A5  |  **Pin 21**   

# Notas de Software
No es necesario modificar los archivos de la librería `FreqCount`, ya que el soporte ya está incluido en el código fuente (`FreqCountTimers.h`). Asegúrate de seleccionar "Arduino Mega or Mega 2560" en tu IDE antes de subir el código.

# Consideraciones sobre el PCB
El diseño de PCB incluido en este proyecto está creado específicamente para el factor de forma del **Arduino Nano**.

    - **Factor de Forma:** El Arduino Mega 2560 es físicamente mucho más grande y tiene una disposición de pines diferente. No encajará en los zócalos diseñados para el Nano.
    - **Incompatibilidad Directa:** Debido a los cambios de pines necesarios (Pin 47 para frecuencia, 20/21 para I2C), las pistas del PCB original no conducen a los lugares correctos en el Mega.

**Recomendación:** Para usar un Arduino Mega, no se puede utilizar el archivo de fabricación de PCB actual. Se recomienda:

    - Utilizar una protoboard o placa de pruebas para realizar el cableado manualmente según la tabla de conexiones.
    - Rediseñar el PCB en KiCad si se desea una solución permanente, adaptando el diseño para que funcione como un "Shield" de Arduino Mega.
