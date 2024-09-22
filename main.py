import subprocess
import os
import xml.etree.ElementTree as ET

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
    projects_directory = "C:\\Users\\gravi\\Desktop\\projects\\asylum\\c# sprints\\"
        # Измени фамилию-имя-отчество на свое
    initials = "KomarovNA"
    initials_ru = "Комаров Никита Алексеевич"
        # !!! ИЗМЕНИ НОМЕР СПРИНТА !!!
    sprint_number = 2
        # change often
        # перед началом нового таска меняй ТЕМУ таска и ОПИСАНИЕ таска. Просто копируй с сайта
    title = "Оператор if - полная и короткая форма записи"
    condition = """
    Написать программу на, которая запрашивает целые значения с клавиатуры и вычисляет находится ли точка с координатами X,Y в заштрихованной области."""
    ### END SETTINGS ###
    
    
    
    def __init__(self):
        task_variant = input('№таска №варианта через пробел:')
        self.task_number, self.variant_number = task_variant.split()
        # self.task_number, self.variant_number = ('2', '17')
        
        self.solution_folder_name = f"Tyuiu.{self.initials}.Sprint{self.sprint_number}"
        self.path = os.path.join(self.projects_directory,self.solution_folder_name)
        self.solution_name = f"Tyuiu.{self.initials}.Sprint{self.sprint_number}.sln"
                
        self.__generate_hello_table()
        self.__generate_app_names()
        self.__generate_programs_code()
        
    def __generate_hello_table(self):
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

        self.console_table = """Console.Title = "Спринт #"""+str(self.sprint_number)+""" | Выполнил: """+self.initials_ru+""" | ИИПБ-24-1";
            //Длинна строки 75 символов
            Console.WriteLine("***************************************************************************");
            Console.WriteLine("* Спринт #"""+str(self.sprint_number)+"""                                                               *");
            Console.WriteLine("* """ + title+' '*(symbols-len(title)) + """*");
            Console.WriteLine("* Задание #"""+task+"""                                                              *");
            Console.WriteLine("* Вариант #"""+variant+f'{" " if len(str(variant))>=2 else ""}'+"""                                                            *");
            Console.WriteLine("* Выполнил: """+self.initials_ru+""" | ИИПБ-24-1                         *");
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
        
        self.library_code = """using tyuiu.cources.programming.interfaces.Sprint"""+str(sprint)+""";

namespace Tyuiu."""+fio+""".Sprint"""+str(sprint)+""".Task"""+str(task)+""".V"""+str(variant)+""".Lib
{
    public class DataService : ISprint"""+str(sprint)+"""Task"""+str(task)+"""V"""+str(variant)+"""
    {

    }
}
"""

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
                    # get .cs file in project directory to modify and rename it
                    file_to_edit_list = [file for file in os.listdir(folder_name) if file.split('.')[-1] == 'cs']
                    file_to_edit = file_to_edit_list[0] if len(file_to_edit_list) >= 1 else None
                    if new_file_name is not None and file_to_edit is not None:
                        os.rename(folder_name+'\\'+file_to_edit, folder_name+'\\'+new_file_name)
                        file_to_edit = new_file_name
                    with open(folder_name+'\\'+file_to_edit, 'w', encoding='utf-8-sig') as file:
                        file.write(file_code)   
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
                    hint_path.text = '..\\tyuiu.cources.programming.interfaces.dll'
                    
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