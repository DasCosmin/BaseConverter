using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Conversii
{
    public partial class FormCalculator : Form
    {
        public string[] possibleBases = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "16" };
        public List<Button> buttons;

        private TextBox currentFocusedTextBox;
        private string operation = "+";

        /// <summary>
        /// The constructor of the FormCalculator class
        /// </summary>
        public FormCalculator()
        {
            InitializeComponent();
            currentFocusedTextBox = textBoxFirstBase;
            buttons = new List<Button>{button0, button1, button2, button3, button4, button5, button6, button7, button8, button9,
                buttonA, buttonB, buttonC, buttonD, buttonE, buttonF};
        }

        /// <summary>
        /// Function which closes the Application by pressing the Exit Button from the Title Bar
        /// </summary>
        private void FormCalculator_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxFirstBase
        /// and turns OFF the buttons corresponding to the hexadecimal digits. 
        /// </summary>
        private void TextBoxFirstBase_Enter(object sender, EventArgs e)
        {
            currentFocusedTextBox = textBoxFirstBase;
            TurnOnOffButtons(10);
        }

        /// <summary>
        /// Function which adds zero to the end of currentFocusedTextBox 
        /// </summary>
        private void button0_Click(object sender, EventArgs e)
        {
            if (currentFocusedTextBox.Text == "") return;
            currentFocusedTextBox.Text += "0";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds one to the end of currentFocusedTextBox 
        /// </summary>
        private void button1_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "1";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function that deletes the last character of a TextBox
        /// </summary>
        /// <param name="textBox">The TextBox to delete the last character for</param>
        private void DeleteLastCharTextBox(TextBox textBox)
        {
            textBox.Text = textBox.Text.Remove(textBox.Text.Length - 1);
        }

        /// <summary>
        /// Function which deletes the last character of currentFocusedTextBox
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (currentFocusedTextBox.Text.Length == 0) return;
            DeleteLastCharTextBox(currentFocusedTextBox);
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxSecondBase
        /// and turns OFF the buttons corresponding to the hexadecimal digits.
        /// </summary>
        private void textBoxSecondBase_Enter(object sender, EventArgs e)
        {
            currentFocusedTextBox = textBoxSecondBase;
            TurnOnOffButtons(10);
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxResultBase
        /// and turns OFF the buttons corresponding to the hexadecimal digits.
        /// </summary>
        private void textBoxResultBase_Enter(object sender, EventArgs e)
        {
            currentFocusedTextBox = textBoxResultBase;
            TurnOnOffButtons(10);
        }

        /// <summary>
        /// Function which adds two to the end of currentFocusedTextBox 
        /// </summary>
        private void button2_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "2";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds three to the end of currentFocusedTextBox 
        /// </summary>
        private void button3_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "3";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds four to the end of currentFocusedTextBox 
        /// </summary>
        private void button4_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "4";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds five to the end of currentFocusedTextBox 
        /// </summary>
        private void button5_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "5";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds six to the end of currentFocusedTextBox 
        /// </summary>
        private void button6_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "6";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds seven to the end of currentFocusedTextBox 
        /// </summary>
        private void button7_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "7";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds eight to the end of currentFocusedTextBox 
        /// </summary>
        private void button8_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "8";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds nine to the end of currentFocusedTextBox 
        /// </summary>
        private void button9_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "9";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Changes the arithmetic operation to addition
        /// </summary>
        private void buttonAdd_Click(object sender, EventArgs e)
        {
            operation = labelOperation.Text = "+";
        }

        /// <summary>
        /// Changes the arithmetic operation to substraction
        /// </summary>
        private void buttonSubstract_Click(object sender, EventArgs e)
        {
            operation = labelOperation.Text = "-";
        }

        /// <summary>
        /// Changes the arithmetic operation to multiplication
        /// </summary>
        private void buttonMultiply_Click(object sender, EventArgs e)
        {
            operation = labelOperation.Text = "*";
        }

        /// <summary>
        /// Changes the arithmetic operation to division
        /// </summary>
        private void buttonDivide_Click(object sender, EventArgs e)
        {
            operation = labelOperation.Text = "/";
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxNumber1
        /// </summary>
        private void textBoxNumber1_Enter(object sender, EventArgs e)
        {
            if (textBoxFirstBase.Text == "")
            {
                currentFocusedTextBox = textBoxFirstBase; // Set the focus to the Text Box referring to the base of the first number
                return; 
            }
            currentFocusedTextBox = textBoxNumber1;
            int baseNumber = Int32.Parse(textBoxFirstBase.Text);
            TurnOnOffButtons(baseNumber);
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxNumber2
        /// </summary>
        private void textBoxNumber2_Enter(object sender, EventArgs e)
        {
            if (textBoxSecondBase.Text == "")
            {
                currentFocusedTextBox = textBoxSecondBase; // Set the focus to the Text Box referring to the base of the second number
                return; 
            }
            currentFocusedTextBox = textBoxNumber2;
            int baseNumber = Int32.Parse(textBoxSecondBase.Text);
            TurnOnOffButtons(baseNumber);
        }

        /// <summary>
        /// Function that deletes the currentFocusedTextBox
        /// </summary>
        private void buttonClearEntry_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text = "";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function that deletes the textBoxNumber1, textBoxNumber2 and textBoxResult
        /// </summary>
        private void buttonClear_Click(object sender, EventArgs e)
        {
            textBoxNumber1.Text = textBoxNumber2.Text = textBoxResult.Text = "";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function that turns ON and OFF the buttons depending on the base;
        /// </summary>
        /// <param name="baseNumber">The base of the number</param>
        private void TurnOnOffButtons(int baseNumber)
        {
            foreach (Button button in buttons)
                button.Enabled = false;
            foreach (Button button in buttons.GetRange(0, baseNumber))
                button.Enabled = true; 
        }

        /// <summary>
        /// Function that verifies whether the content of the textBoxBase is correct or not. 
        /// </summary>
        /// <param name="textBox">The TextBox to be verified</param>
        /// <returns>true if the content is correct, false otherwise</returns>
        private bool VerifyInputTextBoxBase(TextBox textBox)
        {
            if (textBox.Text == "1") // In case the user wants to introduce the base 10/16. 
                return true;
            foreach (string possibleBase in possibleBases)
                if (possibleBase == textBox.Text)
                    return true;
            return false;
        }

        /// <summary>
        /// Function that checks whether the number contains only digits (0, 1, 2, ..., 9, A, B, C, D, E, F, a, b, c, d, e, f)
        /// </summary>
        /// <param name="number">The number to be verified</param>
        /// <returns>true if the number contains only digits, false otherwise</returns>
        private bool VerifyOnlyDigits(string number)
        {
            string possibleDigits = "0123456789ABCDEFabcdef";
            foreach (char digit in number)
                if (possibleDigits.IndexOf(digit) == -1) return false;
            return true; 
        }

        /// <summary>
        /// Function that verifies whether the content of the textBoxNumber is correct or not.
        /// </summary>
        /// <param name="textBoxNumber">The TextBox to be verified</param>
        /// <param name="texBoxBase">The TextBox which contains the base of the number</param>
        /// <returns>true if the content is correct, false otherwise</returns>
        private bool VerifyInputTextBoxNumber(TextBox textBoxNumber, TextBox textBoxBase)
        {
            string number = textBoxNumber.Text;
            int baseNumber = Int32.Parse(textBoxBase.Text);
            if (VerifyOnlyDigits(number) == false) return false; 
            if (baseNumber == 16) return true; // The input is always correct
            foreach (char digit in number)
            {
                int digit_ascii = digit - '0';
                if (digit_ascii >= baseNumber) return false; 
            }
            return true; 
        }

        /// <summary>
        /// Function that verifies whether the user is introducing correct input for the textBoxFirstBase. 
        /// Creates a MessageBox if the input is incorrect.
        /// </summary>
        private void textBoxFirstBase_TextChanged(object sender, EventArgs e)
        {
            if (textBoxFirstBase.Text != "" && VerifyInputTextBoxBase(textBoxFirstBase) == false)
            {
                MessageBox.Show("The base has to be an element of {2, 3, ..., 10, 16}!", "Invalid base");
                textBoxFirstBase.Text = "";
            }
            if (textBoxFirstBase.Text != "" && textBoxFirstBase.Text != "1" && 
                VerifyInputTextBoxNumber(textBoxNumber1, textBoxFirstBase) == false) // The digits of the first number are no longer valid 
                    textBoxNumber1.Text = "";
            
        }

        /// <summary>
        /// Function that verifies whether the user is introducing correct input for the textBoxSecondBase. 
        /// Creates a MessageBox if the input is incorrect.
        /// </summary>
        private void textBoxSecondBase_TextChanged(object sender, EventArgs e)
        {
            if (textBoxSecondBase.Text != "" && VerifyInputTextBoxBase(textBoxSecondBase) == false)
            {
                MessageBox.Show("The base has to be an element of {2, 3, ..., 10, 16}!", "Invalid base");
                textBoxSecondBase.Text = "";
            }
            if (textBoxSecondBase.Text != "" && textBoxSecondBase.Text != "1" &&
                VerifyInputTextBoxNumber(textBoxNumber2, textBoxSecondBase) == false) // The digits of the second number are no longer valid 
                textBoxNumber2.Text = "";
        }

        /// <summary>
        /// Function that verifies whether the user is introducing correct input for the textBoxResultBase
        /// Creates a MessageBox if the input is incorrect.
        /// </summary>
        private void textBoxResultBase_TextChanged(object sender, EventArgs e)
        {
            if (textBoxResultBase.Text != "" && VerifyInputTextBoxBase(textBoxResultBase) == false)
            {
                MessageBox.Show("The base has to be an element of {2, 3, ..., 10, 16}!", "Invalid base");
                textBoxResultBase.Text = "";
            }
        }

        /// <summary>
        /// Function which adds the hexadecimal digit A to the end of currentFocusedTextBox 
        /// </summary>
        private void buttonA_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "A";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }
        
        /// <summary>
        /// Function which adds the hexadecimal digit B to the end of currentFocusedTextBox 
        /// </summary>
        private void buttonE_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "E";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds the hexadecimal digit C to the end of currentFocusedTextBox 
        /// </summary>
        private void buttonD_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "D";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds the hexadecimal digit D to the end of currentFocusedTextBox 
        /// </summary>
        private void buttonF_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "F";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds the hexadecimal digit E to the end of currentFocusedTextBox 
        /// </summary>
        private void buttonB_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "B";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function which adds the hexadecimal digit F to the end of currentFocusedTextBox 
        /// </summary>
        private void buttonC_Click(object sender, EventArgs e)
        {
            currentFocusedTextBox.Text += "C";
            currentFocusedTextBox.Focus();
            currentFocusedTextBox.SelectionStart = currentFocusedTextBox.Text.Length;
        }

        /// <summary>
        /// Function that verifies whether the user is introducing correct input for the textBoxNumber1
        /// Creates a MessageBox if the input is incorrect.
        /// </summary>
        private void textBoxNumber1_TextChanged(object sender, EventArgs e)
        {
            if (VerifyInputTextBoxNumber(textBoxNumber1, textBoxFirstBase) == false)
            {
                DeleteLastCharTextBox(textBoxNumber1);
                MessageBox.Show("Incorrect digit! The base is " + textBoxFirstBase.Text + "!", "Invalid digit");
            }
            textBoxNumber1.Text = textBoxNumber1.Text.ToUpper();
            textBoxNumber1.SelectionLength = 0;
            textBoxNumber1.SelectionStart = textBoxNumber1.Text.Length;
            textBoxHEX.Text = textBoxDEC.Text = textBoxBIN.Text = textBoxResult.Text = "";
        }

        private void textBoxNumber2_TextChanged(object sender, EventArgs e)
        {
            if (VerifyInputTextBoxNumber(textBoxNumber2, textBoxSecondBase) == false)
            {
                DeleteLastCharTextBox(textBoxNumber2);
                MessageBox.Show("Incorrect digit! The base is " + textBoxSecondBase.Text + "!", "Invalid digit");
            }
            textBoxNumber2.Text = textBoxNumber2.Text.ToUpper();
            textBoxNumber2.SelectionLength = 0;
            textBoxNumber2.SelectionStart = textBoxNumber2.Text.Length;
            textBoxHEX.Text = textBoxDEC.Text = textBoxBIN.Text = textBoxResult.Text = "";
        }

        private void buttoneEqual_Click(object sender, EventArgs e)
        {
            try
            {
                // Determine the path of the Directory where the Python Interpreter and the Python App are located 
                string path = Directory.GetCurrentDirectory();
                int position = path.IndexOf(@"\bin\Debug");
                path = path.Remove(position);

                // Full path of Python Interpreter 
                string python = path + @"\Python\Python37\python.exe";

                // Full path of Python App for conversion
                string myPythonApp = path + @"\ConversionOperations\main.py";

                // Parameters to be sent to the script 
                string numberA = textBoxNumber1.Text;
                string numberB = textBoxNumber2.Text;
                int base_numberA = Int32.Parse(textBoxFirstBase.Text);
                int base_numberB = Int32.Parse(textBoxSecondBase.Text);
                int base_result = Int32.Parse(textBoxResultBase.Text);

                // Create new process start info 
                ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);

                // Make sure the output can be read from stdout 
                myProcessStartInfo.UseShellExecute = false;
                myProcessStartInfo.RedirectStandardOutput = true;
                myProcessStartInfo.CreateNoWindow = true;

                // Start Python App with 7 arguments  
                // 1st arguments is pointer to itself,  
                // the rest are the actual arguments to be sent. 
                myProcessStartInfo.Arguments = myPythonApp + " " + operation + " " + base_numberA + " " + base_numberB + " " + base_result + " " +
                    numberA + " " + numberB;

                Process myProcess = new Process();
                // Assign start information to the process 
                myProcess.StartInfo = myProcessStartInfo;

                // Start the process 
                myProcess.Start();

                // Read the standard output of the Python App.  
                // In order to avoid deadlock it will read output first 
                // and then wait for process to terminate: 
                StreamReader myStreamReader = myProcess.StandardOutput;
                string finalResults = myStreamReader.ReadLine();
                string[] results = finalResults.Split('|'); // | is used as a delimiter between the 4 results

                // Wait for exit signal from the Python App and then close it. 
                myProcess.WaitForExit();
                myProcess.Close();

                // Update textBoxes
                textBoxResult.Text = results[0];
                textBoxHEX.Text = results[1];
                textBoxDEC.Text = results[2];
                textBoxBIN.Text = results[3];
            }
            catch (IndexOutOfRangeException)
            {

            }
        }
    }
}
