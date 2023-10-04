// Task1.cs

namespace windowsFormsGettingHangOf
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            textBox1.Focus();
            textBox2.Text = "Waiting for input...";
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void duplicateText(string text)
        {
            if (text.Length > 0 && text != null && text != "Input stuff here...")
            {
                textBox2.Text = text;
            }
            else
            {
                textBox1.Text = "Input stuff here...";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string inputText = textBox1.Text;
                duplicateText(inputText);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Something went wrong...", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                duplicateText(textBox1.Text);
            }
        }

        private void textBox2_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                textBox2.Text = "This one is for output...";
            }
        }
    }
}