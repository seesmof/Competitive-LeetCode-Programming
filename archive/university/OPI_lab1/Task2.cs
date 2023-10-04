// Task2.cs

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
            textBox1.Focus();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            textBox2.Text = textBox1.Text;
        }

        private void MainForm_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
        }

        private void textBox2_KeyDown(object sender, KeyEventArgs e)
        {
            closeOnEscape(sender, e);
            textBox2.Text = "This one is for output...";
        }
    }
}