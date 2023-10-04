// Task3.cs

namespace windowsFormsGettingHangOf
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void closeOnEscape(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                Close();
            }
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            label2.Visible = false;
            checkBox1.Checked = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                if (comboBox1.SelectedItem != null)
                {
                    label2.Visible = true;
                    textBox1.Text = comboBox1.SelectedItem.ToString();
                    string sportNameToLowercase = textBox1.Text!.ToLower();
                    label2.Text = "Your favorite sport is " + sportNameToLowercase + "!";
                }
                else
                {
                    MessageBox.Show("Please select your favorite sport", "ERROR: Sport not selected", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                MessageBox.Show("Please tick the checkbox to see your favorite sport", "ERROR: Checkbox not ticked", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void MainForm_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void comboBox1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void button1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }
    }
}