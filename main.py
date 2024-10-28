import subprocess
import os
import xml.etree.ElementTree as ET
import json


class Program:
    """
        Для изменения:
            1 раз поменять
                - директория со всеми солюшинами(спринтами)
                - фамилия-имя-отчество
            1 раз в 7 раз
                - номер спринта
            каждый раз
                - тема и описание таска
                - номер варианта и таска (в консоли при запуске)
    """
    ### SETTINGS ###
        # Поменяй projects_directory на папку, где лежат все спринты. Не конкретный открытый спринт 
        # !!! ОБЯЗАТЕЛЬНО В ПУТИ ДОЛЖНО БЫТЬ ДВА СЛЭША '\\' , НЕ ОДИН !!!
        # ЛИБО оставь projects_directory пустым и закинь файл в папку со всеми solution(спринтами)
    projects_directory = "C:\\Users\\gravi\\Desktop\\projects\\asylum\\c# sprints"
        # Измени фамилию-имя-отчество на свое
    initials = "KomarovNA"
    initials_ru = "Комаров Никита Алексеевич"
    group = "ИИПБ-24-1"
        # !!! ИЗМЕНИ НОМЕР СПРИНТА !!!
    sprint_number = 5
        # change often
        # перед началом нового таска меняй ТЕМУ таска и ОПИСАНИЕ таска. Просто копируй с сайта
    title = ""
    condition = """
    """
    ### END SETTINGS ###
    
    
    
    def __init__(self):
        # read config from json
        config_file = 'config.json'
        try:
            with open(config_file, encoding='utf-8-sig') as json_data:
                data = json.load(json_data)
                self.projects_directory = data.get('projects_directory', '')
                self.sprint_number = data.get('sprint_number', '')
                self.initials = data.get('initials', '')
                self.initials_ru = data.get('initials_ru', '')
                self.group = data.get("group", '')
                self.title = data.get('title', '')
                self.condition = data.get('condition', '')
        except:
            print("!"*40+"\nОТСТУТСТВУЕТ ФАЙЛ КОНФИГУРАЦИИ config.json \nБудет применена стандартная конфигурация из кода. СОЗДАЙТЕ ФАЙЛ config.json\n"+'!'*40)
        
        # read input task and variant numbers
        task_var_list = input('№таска №варианта через пробел:').split()
        while True:
            if len(task_var_list) == 2:
                task_num, task_var = task_var_list
                if task_num.isdigit() and task_var.isdigit():
                    break
                else:
                    print("Номер таска и номер варианта должны быть числом.")
            else:
                print("Нужно ввести 2 значения: номер таска и номер варианта.")
            task_var_list = input('\n№таска №варианта через пробел:').split()
            
        self.task_number, self.variant_number = task_var_list
        
        self.solution_folder_name = f"Tyuiu.{self.initials}.Sprint{self.sprint_number}"
        self.path = os.path.join(self.projects_directory,self.solution_folder_name)
        self.solution_name = f"Tyuiu.{self.initials}.Sprint{self.sprint_number}.sln"
        
        self.shit_dll = 'tyuiu.cources.programming.interfaces.dll'
               
        self.__generate_hello_table()
        self.__generate_app_names()
        self.__generate_programs_code()
        
    def __generate_hello_table(self):
        if (self.sprint_number == 6) :
          self.console_table = ""
          return
        condition = self.condition
        title = self.title
        task = self.task_number
        variant = self.variant_number
        new_str = ''
        for line in condition.split('\n'):
            line = line.strip()
            if line and line !='\n' and line!=0:
                new_str = new_str + line + ' '
            
        final_str = ''
        symbols = 72
        max_operations = (len(new_str) // symbols) + 1

        current_indx = 0
        for i in range(max_operations):
            text = new_str[0:symbols+1]
            if(len(text) < symbols):
                text += ' '*(symbols-len(text)+1)
            new_str = new_str[symbols:]
            final_str = final_str + ' '*4*3 + 'Console.WriteLine("*' + text + '*");' + '\n'
            
            current_indx += symbols

        self.console_table = """Console.Title = "Спринт #"""+str(self.sprint_number)+""" | Выполнил: """+self.initials_ru+""" | """+self.group+"""";
            //Длинна строки 75 символов
            Console.WriteLine("***************************************************************************");
            Console.WriteLine("* Спринт #"""+str(self.sprint_number)+"""                                                               *");
            Console.WriteLine("* """ + title+' '*(symbols-len(title)) + """*");
            Console.WriteLine("* Задание #"""+task+"""                                                              *");
            Console.WriteLine("* Вариант #"""+variant+f'{" " if len(str(variant))>=2 else ""}'+"""                                                            *");
            Console.WriteLine("* Выполнил: """+self.initials_ru+""" | """+self.group+"""                         *");
            Console.WriteLine("***************************************************************************");
            Console.WriteLine("* УСЛОВИЕ:                                                                *"); 
            """ + '\n' + final_str + """
            """ + """Console.WriteLine("*                                                                         *");
            Console.WriteLine("***************************************************************************");
            Console.WriteLine("* ИСХОДНЫЕ ДАННЫЕ:                                                        *");
            Console.WriteLine("***************************************************************************");

            Console.WriteLine("***************************************************************************");
            Console.WriteLine("*                                                                         *");
            Console.WriteLine("***************************************************************************");

            Console.WriteLine("***************************************************************************");
            Console.WriteLine("* РЕЗУЛЬТАТ:                                                              *");
            Console.WriteLine("***************************************************************************");"""

    def __generate_app_names(self):
        sprint = self.sprint_number
        task = self.task_number
        variant = self.variant_number
        fio = self.initials
        self.console_app_name = f"Tyuiu.{fio}.Sprint{sprint}.Task{task}.V{variant}"
        self.library_name = f"Tyuiu.{fio}.Sprint{sprint}.Task{task}.V{variant}.Lib"
        self.mstest_name = f"Tyuiu.{fio}.Sprint{sprint}.Task{task}.V{variant}.Test"
 
    def __generate_programs_code(self):
        sprint = self.sprint_number
        task = self.task_number
        variant = self.variant_number
        fio = self.initials
        if (self.sprint_number != 6): # Generate general console app code
            self.console_app_code = """using Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""".Lib;
namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+"""
{
    class Program
    {
        static void Main(string[] args)
        {
            """+self.console_table+"""

            DataService ds = new DataService();

            var result = ds.YOURFUNCTION();
            Console.WriteLine(result);
            Console.ReadKey();
        }
    }
}"""
        else: # GENERATE CODE FOR WINFORMS APP IN 6 SPRINT
            self.console_app_code = ""
            self.form_main_code = """using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""".Lib;

namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+"""
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
        }

        DataService ds = new DataService();
    }
}"""
            self.form_designer_code = """namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""";
            
partial class FormMain
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.components = new System.ComponentModel.Container();
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(800, 450);
        this.Text = "Form1";
    }

    #endregion
}"""        

            self.program_code = """using Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""".Lib;
namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+"""
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            Application.Run(new FormMain());
        }
    }
}"""
            
            ### END 6 SPRINT CODE GENERATING ###
            
		# GENERATE LIBRARY CODE
        self.library_code = """using tyuiu.cources.programming.interfaces.Sprint"""+str(sprint)+""";

namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""".Lib
{
    public class DataService : ISprint"""+str(sprint)+"""Task"""+str(task)+"""V"""+str(variant)+"""
    {

    }
}
"""
		# GENERATE MSTEST CODE
        self.mstest_code = """namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""".Test
{
    public class DataServiceTest
    {
        public void TestMethod1()
        {
            Assert.AreEqual(1, 1);
        }
    }
}"""
    
    def __create_solution(self):
        solution_exists = os.path.exists(self.path+'\\'+self.solution_name)
        if not solution_exists:
            os.makedirs(self.path)
            os.chdir(self.path)
            command = f"dotnet new sln -n {self.solution_folder_name}"
            process = subprocess.run(command, shell=True, check=True)
            if process.returncode == 0:
                print(f"Solution {self.solution_folder_name} был успешно создан!")
            else:
                print("Ошибка при создании solution.")
                
    def __copy_dll(self):
        path = f"{self.path[:-1] + str(self.sprint_number-1)}\\{self.shit_dll}"
        if os.path.exists(path):
            os.system(f'copy "{path}" "{os.path.join(self.path, self.shit_dll)}"')
    
    def __create_projects(self):
        console_app_exists = os.path.exists(self.path+'\\'+self.console_app_name)
        library_exists = os.path.exists(self.path+'\\'+self.library_name)
        mstest_name_exists = os.path.exists(self.path+'\\'+self.mstest_name)
        projects_dicts = (
            {
                "library": {
                    'terminal': 'classlib',
                    'folder_name': self.library_name,
                    'file_code': self.library_code,
                    'exists': library_exists,
                    'file_to_edit': 'Class1.cs',
                    'new_file_name': 'DataService.cs',
                    },
                "console_app": {
                    'terminal': 'console',
                    'folder_name': self.console_app_name,
                    'file_code': self.console_app_code,
                    'file_to_edit': 'Program.cs',
                    'exists': console_app_exists,
                    },
                "mstest": {
                    'terminal': 'mstest',
                    'folder_name': self.mstest_name,
                    'file_code': self.mstest_code,
                    'exists': mstest_name_exists,
                    'file_to_edit': 'UnitTest1.cs',
                    'new_file_name': 'DataServiceTest.cs',
                    },
                }
        )
        if self.sprint_number == 6:
            projects_dicts['console_app'] = {
				'terminal': 'winforms',
				'folder_name': self.console_app_name,
				'file_to_edit': ('Form1.cs', 'Form1.Designer.cs', 'Program.cs'),
				'file_code': {
                    'Form1.cs': self.form_main_code,
                    'Form1.Designer.cs': self.form_designer_code, 
                    'Program.cs': self.program_code
                    },
				'new_file_name': {
                    'Form1.cs': 'FormMain.cs',
                    'Form1.Designer.cs': 'FormMain.Designer.cs'
                    },
				'exists': console_app_exists,
			}
        # create and modify projects: console_app, library, mstest
        for project_name, project_dict in projects_dicts.items():
            terminal = project_dict['terminal']
            folder_name = project_dict['folder_name']
            exists = project_dict['exists']
            file_code = project_dict['file_code']
            file_to_edit = project_dict['file_to_edit']
            new_file_name = project_dict.get('new_file_name', None)
            
            # create projects folders
            if not exists:
                command1 = f"dotnet new {terminal} -n {folder_name}"
                command2 = f"dotnet sln {self.solution_name} add {folder_name}\\{folder_name}.csproj"
                process1 = subprocess.run(command1, shell=True, check=True)
                process2 = subprocess.run(command2, shell=True, check=True)
                if process1.returncode == 0 and process2.returncode == 0:
                    print(f"Проект {project_name}: '{folder_name}' был успешно создан!")
                else:
                    print(f"Ошибка при создании проекта {project_name}: '{folder_name}'")
            
                # rewrite the code    
                try:
                    # for all sprint except 6 do the old code to not break the program
                    if (self.sprint_number != 6 or project_name!='console_app'):
                        # get .cs file in project directory to modify and rename it
                        file_to_edit_list = [file for file in os.listdir(folder_name) if file.split('.')[-1] == 'cs']
                        file_to_edit = file_to_edit_list[0] if len(file_to_edit_list) >= 1 else None
                        if new_file_name is not None and file_to_edit is not None:
                            os.rename(folder_name+'\\'+file_to_edit, folder_name+'\\'+new_file_name)
                            file_to_edit = new_file_name
                        with open(folder_name+'\\'+file_to_edit, 'w', encoding='utf-8-sig') as file:
                            file.write(file_code)
                    # new code for 6 sprint
                    else:
                        for file in file_to_edit:
                            # rewrite the code
                            if file_code is not None and file is not None:
                                if file_code.get(file, None) is not None:
                                    with open(folder_name+'\\'+file, 'w', encoding='utf-8-sig') as f:
                                        f.write(file_code[file])
                            # rename file
                            if new_file_name is not None and file is not None:
                                if new_file_name.get(file, None) is not None:  
                                    os.rename(folder_name+'\\'+file, folder_name+'\\'+new_file_name[file])
                    print("Файлы успешно отредактированы.")
                        
                except:
                    print("Ошибка при редактиваровании файлов проекта.")
            else:
                print(f'Проект {project_name} уже существует.')
                
            # add reference
            csproj_source, csproj_destination = None, None
            if project_name == 'console_app':
                csproj_source = folder_name+'\\'+folder_name+'.csproj'
                dest_folder = projects_dicts['library']['folder_name']
                csproj_destination = dest_folder+'\\'+dest_folder+'.csproj'
            if csproj_source and csproj_destination:
                command = f"dotnet add {csproj_source} reference {csproj_destination}"
                process = subprocess.run(command, shell=True, check=True)
                if process.returncode == 0:
                    print(f"Зависимость {csproj_destination} добавлена в проект {project_name}")
                else:
                    print(f"Ошибка при добавлении зависимости {csproj_destination} в проект {project_name}'")
            
            # add custom reference. Shit dll
            if project_name == 'library':
                csproj_source = folder_name+'\\'+folder_name+'.csproj'
                try:
                    tree = ET.parse(csproj_source)
                    root = tree.getroot()
                    
                    # create ItemGroup for .csproj
                    item_group = ET.Element('ItemGroup')
                    reference = ET.SubElement(item_group, 'Reference', Include="tyuiu.cources.programming.interfaces")
                    hint_path = ET.SubElement(reference, 'HintPath')
                    hint_path.text = f'..\\{self.shit_dll}'
                    
                    for element in root:
                        if element.tag == 'PropertyGroup':
                            root.insert(list(root).index(element) + 1, item_group)
                            break
                    
                    tree.write(csproj_source, encoding="utf-8", xml_declaration=True)
                    print("Dll Спирина добавлена в проект.")
                except:
                    print("Ошибка в добавлении ссылки на библиотеку дерьма (dll Спирина).")

    def create(self):
        self.__create_solution()
        self.__copy_dll()
        os.chdir(self.path)
        self.__create_projects()
        
    
    def display(self):
        print(self.console_app_name)
        print(self.library_name)
        print(self.mstest_name)
        print(self.console_app_code)
        print(self.library_code)
        print(self.mstest_code)
    
prog = Program()
# prog.display()
prog.create()
input('Enter to close')