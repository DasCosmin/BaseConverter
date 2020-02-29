using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Conversii
{
    public partial class FormCalculator : Form
    {
        private TextBox currentFocusedTextBox;

        /// <summary>
        /// The constructor of the FormCalculator class
        /// </summary>
        public FormCalculator()
        {
            InitializeComponent();
            currentFocusedTextBox = textBoxFirstBase;
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
        /// </summary>
        private void textBoxFirstBase_Enter(object sender, EventArgs e)
        {
            currentFocusedTextBox = textBoxFirstBase;
        }

        /// <summary>
        /// Function which adds zero to the end of currentFocusedTextBox 
        /// </summary>
        private void button0_Click(object sender, EventArgs e)
        {
            if (currentFocusedTextBox.Text == "") return;
            if (currentFocusedTextBox.Text.Length == 2) return;
            currentFocusedTextBox.Text += "0";
        }

        /// <summary>
        /// Function which adds one to the end of currentFocusedTextBox 
        /// </summary>
        private void button1_Click(object sender, EventArgs e)
        {
            if (currentFocusedTextBox.Text.Length == 2) return;
            currentFocusedTextBox.Text += "1";
        }

        /// <summary>
        /// Function which deletes the last character of currentFocusedTextBox
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (currentFocusedTextBox.Text.Length == 0) return;
            currentFocusedTextBox.Text = currentFocusedTextBox.Text.Remove(currentFocusedTextBox.Text.Length - 1);
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxSecondBase
        /// </summary>
        private void textBoxSecondBase_Enter(object sender, EventArgs e)
        {
            currentFocusedTextBox = textBoxSecondBase;
        }

        /// <summary>
        /// Function which changes the currentFocusedTextBox to the textBoxResultBase
        /// </summary>
        private void textBoxResultBase_Enter(object sender, EventArgs e)
        {
            currentFocusedTextBox = textBoxResultBase;
        }

        /// <summary>
        /// Function which adds two to the end of currentFocusedTextBox 
        /// </summary>
        private void button2_Click(object sender, EventArgs e)
        {
            if (currentFocusedTextBox.Text.Length == 2) return; 
            currentFocusedTextBox.Text += "2";
        }
    }
}
