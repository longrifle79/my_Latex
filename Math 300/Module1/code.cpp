#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <QTextStream>
#include <QDebug>
#include <QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QtWidgets>
#include <QPixmap>

// Register and pin definitions
#define CMD_ARFE_TYPE       0x0000
#define ENABLE_PIN          (1U << 31)

// Device addresses
#define ASA_ADDRESS         64
#define CHAMBER_MONITOR_ADDRESS    33
#define CIMOD_ADDRESS             192
#define CIRFU_ADDRESS             212
#define COMBINER_TRAY_ADDRESS     232
#define CONFIG_MATRIX_ADDRESS     25
#define DICE_ADDRESS             189
#define FPCD_ADDRESS             96
#define JAMMER_MATRIX_ADDRESS    37
#define MONITOR_MATRIX_ADDRESS   21
#define OSCILLATOR_DRAWER_ADDRESS 16
#define XMOD_ADDRESS            128
#define XRFU_ADDRESS            160

// LED Modes
#define ETHERNET_CONTROL    0x00U
#define COUNT_UP            0x01U
#define COUNT_DOWN          0x02U
#define COUNT_IN            0x03U
#define FLASH_ALL           0x04U
#define FLASH_EVEN_ODD      0x05U
#define JUMP_AROUND         0x06U
#define GLOW                0x07U
#define HEARTBEAT_MSB       0x08U

QString IPadd;  // Stores IP address of the selected device
quint16 IOreg = 0x00F;      // I/O register address
quint64 regVal = 0x02;      // Register value
quint64 pinNum = 0x008;     // Pin number
unsigned long delay = 1000; // Delay time in milliseconds

/**
 * @brief Event-driven functions for UI interactions
 */

/**
 * @brief Sets a selected pin to HIGH when Test IO Set button is clicked
 * @details Retrieves the current pin index from cb_arfe_io_pin_Number combo box,
 * adds 8 to map UI selection to actual pin numbers, and calls setPinHigh()
 * @note Connected to QPushButton clicked signal for testing pin setting
 */
void MainWindow::on_PB_Test_IO_Set_clicked()
{
    setPinHigh((int)ui->cb_arfe_io_pin_Number->currentIndex() + 8);
}

/**
 * @brief Sets a selected pin to LOW when Test IO Set 2 button is clicked
 * @details Similar to on_PB_Test_IO_Set_clicked but calls setPinLow() instead
 * @note Provides complementary functionality to test clearing a pin
 */
void MainWindow::on_PB_Test_IO_Set_2_clicked()
{
    setPinLow((int)ui->cb_arfe_io_pin_number->currentIndex() + 8);
}

/**
 * @brief Enables all IO pins when Enable Pin button is clicked
 * @details Simply calls EnableIOPins() to activate pin functionality
 * @note Acts as UI trigger for enabling pins
 */
void MainWindow::on_PB_Enable_Pin_clicked()
{
    EnableIOPins();
}

/**
 * @brief Clears all registers when Clear All Registers button is clicked
 * @details Calls clearAll() to reset the system to a known state
 * @note Provides quick system reset functionality
 */
void MainWindow::on_PB_ClearAllRegisters_clicked()
{
    clearAll();
}

/**
 * @brief Updates IP address display when device type selection changes
 * @param index The selected index in the combo box
 * @details Gets box number offset from another combo box, looks up IP address
 * in 2D array arfe_io_box_type using type (index) and number (offset), and
 * updates line edit widget
 * @note Manages IP address selection for different device types
 */
void MainWindow::on_CB_ARFI_IO_Box_Select_CurrentIndexChanged(int index)
{
    int box_offset = ui->CB_ARFI_IO_Box_number_select->currentIndex();
    IPadd = arfe_io_box_type.at(index).at(box_offset);
    ui->le_arfe_io_ipAdd->setText(IPadd);
}

/**
 * @brief Updates IP address when device number selection changes
 * @param index The selected index in the combo box
 * @details Similar to on_CB_ARFI_IO_Box_Select but with swapped indices
 * @note Provides complementary selection for device numbering
 */
void MainWindow::on_CB_ARFI_IO_Box_Number_Select_currentIndexChanged(int index)
{
    int box = ui->CB_ARFI_IO_Box_Select->currentIndex();
    IPadd = arfe_io_box_type.at(box).at(index);
    ui->le_arfe_io_ipAdd->setText(IPadd);
}

/**
 * @brief Creates flashing effect on selected pin when flash button is clicked
 * @details Gets delay from slider (multiplied by 10), loops 10 times setting
 * pin high then low with delays using QThread::msleep()
 * @note Implements basic LED flash pattern with adjustable speed
 */
void MainWindow::on_pb_arfe_flash_clicked()
{
    delay = ui->hslide_arfe_io_delay_slider->value() * 10;
    for(int i = 0; i < 10; i++)
    {
        setPinHigh((int)ui->cb_arfe_io_pin_Number->currentIndex() + 8);
        QThread::msleep(delay);
        setPinLow((int)ui->cb_arfe_io_pin_Number->currentIndex() + 8);
        QThread::msleep(delay);
    }
}

/**
 * @brief Creates Knight Rider scanning effect when button is pressed
 * @details Runs 10 cycles of scanning pins 8-15 left to right then right to left,
 * setting each pin high then low with configurable delay
 * @note Mimics classic KITT car light effect from the TV show
 */
void MainWindow::on_pb_arfe_io_knight_rider_pressed()
{
    for(int i = 0; i < 10; i++)
    {
        delay = ui->hslide_arfe_io_delay_slider->value() * 10;
        for(int i = 8; i < 16; i++)
        {
            setPinHigh(i);
            QThread::msleep(delay);
            setPinLow(i);
            QThread::msleep(delay);
        }
        
        for(int i = 14; i > 7; i--)
        {
            setPinHigh(i);
            QThread::msleep(delay);
            setPinLow(i);
            QThread::msleep(delay);
        }
    }
}

/**
 * @brief Creates fade effect by varying delay times when fade button is clicked
 * @details Runs 10 cycles, each with 10 steps of increasing delays (0-9ms),
 * setting pin high then low
 * @note Creates pulsing effect that speeds up/slows down
 */
void MainWindow::on_pb_arfe_io_fade_clicked()
{
    for(int j = 0; j < 10; j++)
    {
        for(int i = 0; i < 10; i++)
        {
            setPinHigh((int)ui->cb_arfe_io_pin_Number->currentIndex() + 8);
            QThread::msleep(i);
            setPinLow((int)ui->cb_arfe_io_pin_Number->currentIndex() + 8);
            QThread::msleep(i);
        }
    }
}

/**
 * @brief Pin setting functions
 */

/**
 * @brief Sets a specific pin to HIGH state
 * @param pin The pin number to set high
 * @details Reads current register value, uses bitwise OR to set specified pin bit,
 * and writes new value back to hardware
 * @note Performs low-level bit manipulation for pin control
 */
void MainWindow::setPinHigh(quint64 pin)
{
    quint64 registerValue;
    TMObject.MotherBoard_ReadSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
    registerValue |= (1U << pin);
    TMObject.MotherBoard_WriteSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
}

/**
 * @brief Sets a specific pin to LOW state
 * @param pin The pin number to set low
 * @details Reads current register value, uses bitwise AND with inverted bit to clear
 * the pin, and writes new value back
 * @note Complementary to setPinHigh for clearing bits
 */
void MainWindow::setPinLow(quint64 pin)
{
    quint64 registerValue;
    TMObject.MotherBoard_ReadSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
    registerValue &= ~(1U << pin);
    TMObject.MotherBoard_WriteSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
}

/**
 * @brief Enable/Disable functions
 */

/**
 * @brief Enables all IO pins
 * @details Reads current register value, sets ENABLE_PIN bit (bit 31) using bitwise OR,
 * and writes value back
 * @note Uses dedicated enable bit to activate IO functionality
 */
void MainWindow::EnableIOPins()
{
    quint64 registerValue;
    TMObject.MotherBoard_ReadSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
    registerValue |= ENABLE_PIN;
    TMObject.MotherBoard_WriteSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
}

/**
 * @brief Disables all IO pins
 * @details Reads current register value, clears ENABLE_PIN bit using bitwise AND with
 * inverted bit, and writes value back
 * @note Opposite of EnableIOPins
 */
void MainWindow::DisableIOPins()
{
    quint64 registerValue;
    TMObject.MotherBoard_ReadSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
    registerValue &= ~ENABLE_PIN;
    TMObject.MotherBoard_WriteSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
}

/**
 * @brief Resets all IO pins to low and disables them
 * @details Reads current register value, uses bitwise AND with inverted mask to clear
 * specific bits (0-15, 23-27), writes value back, and calls DisableIOPins()
 * @note Provides complete reset of IO system
 */
void MainWindow::clearAll(void)
{
    quint64 registerValue;
    TMObject.MotherBoard_ReadSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
    registerValue &= ~( (1U << 0)  | (1U << 1)  | (1U << 2)  | (1U << 3)  |
                        (1U << 4)  | (1U << 5)  | (1U << 6)  | (1U << 7)  |
                        (1U << 8)  | (1U << 9)  | (1U << 10) | (1U << 11) |
                        (1U << 12) | (1U << 13) | (1U << 14) | (1U << 15) |
                        (1U << 24) | (1U << 25) | (1U << 26) | (1U << 27) |
                        (1U << 23));
    TMObject.MotherBoard_WriteSingleRegister(IPadd, IOreg, registerValue, CMD_ARFE_TYPE);
    DisableIOPins();
}

/**
 * @brief Initializes IP address lists for all device types
 * @details Uses QStringList to store IP addresses for each device type and creates
 * a master 2D list (arfe_io_box_type) containing all type lists
 * @note Sets up IP address database for device selection
 */
void MainWindow::ARFE_IO_init(void)
{
    arfe_io_asa_ip << "192.168.100.64" << "192.168.100.65" << "192.168.100.66" << "192.168.100.67" 
                   << "192.168.100.68" << "192.168.100.69" << "192.168.100.70";
    arfe_io_chamberMonitor_ip << "192.168.100.33" << "192.168.100.34" << "192.168.100.35" 
                             << "192.168.100.36" << "192.168.100.37" << "192.168.100.38" 
                             << "192.168.100.39";
    // ... (similar initialization for other device types)
    
    arfe_io_box_type << arfe_io_asa_ip << arfe_io_chamberMonitor_ip << arfe_io_cimod_ip 
                    << arfe_io_cirfu_ip << arfe_io_combiner_tray_ip << arfe_io_config_matrix_ip 
                    << arfe_io_dice_ip << arfe_io_fpcd_ip << arfe_io_jammer_matrix_ip 
                    << arfe_io_monitor_matrix_ip << arfe_io_oscillator_drawer_ip 
                    << arfe_io_xmod_ip << arfe_io_xrfu_ip;
}