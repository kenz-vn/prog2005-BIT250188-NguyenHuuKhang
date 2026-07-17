#include <iostream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

class User {
private:
    string id;
    string name;
    string role;

public:
    User() {}

    // Constructor khởi tạo thông tin người dùng
    User(string id, string name, string role) {
        this->id = id;
        this->name = name;
        this->role = role;
    }

    void display() const {
        cout << id << " - " << name << " - " << role << endl;
    }

    string getId() const {
        return id;
    }

    string getName() const {
        return name;
    }
};

class Task {
private:
    string id;
    string title;
    string status;
    string deadline;

public:
    Task() {}
    Task(string id, string title, string status, string deadline) {
        this->id = id;
        this->title = title;
        this->status = status;
        this->deadline = deadline;
    }

    void display() const {
        cout << "Task: " << title
             << " | Status: " << status
             << " | Deadline: " << deadline << endl;
    }
};

class Project {
private:
    string id;
    string name;
    User manager;
    vector<Task> tasks;

public:
    Project() {}
    Project(string id, string name, User manager) {
        this->id = id;
        this->name = name;
        this->manager = manager;
    }

    void addTask(Task t) {
        tasks.push_back(t);
    }

    string getID() const {
        return id;
    }

    string getName() const {
        return name;
    }

    void display() const {
        cout << "\n===== PROJECT =====\n";
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Manager: ";
        manager.display();

        cout << "\nTask List:\n";
        if (tasks.empty()) {
            cout << "No tasks\n";
        } else {
            for (const Task& t : tasks) {
                t.display();
            }
        }
    }
};

class ProjectManager {
private:
    vector<Project> projects;

public:
    void addProject(Project p) {
        projects.push_back(p);
    }

    void addTaskToProject(string projectId, Task task) {
        for (Project& p : projects) {
            if (p.getID() == projectId) {
                p.addTask(task);
                cout << "Cong viec da duoc them thanh cong.\n";
                return;
            }
        }
        cout << "Du an khong ton tai.\n";
    }

    void displayProjects() {
        if (projects.empty()) {
            cout << "Khong co du an!\n";
            return;
        }

        for (Project p : projects) {
            p.display();
        }
    }

    void findProject(string id) {
        for (Project p : projects) {
            if (p.getID() == id) {
                p.display();
                return;
            }
        }

        cout << "Du an khong ton tai.\n";
    }
};

string inputLine(const string& prompt) {
    cout << prompt;
    string value;
    getline(cin, value);
    return value;
}

int main() {
    ProjectManager app;
    int choice;

    do {
cout << "\n===== PROJECT MANAGEMENT SYSTEM =====\n";
        cout << "1. them du an\n";
        cout << "2. them cong viec vao du an\n";
        cout << "3. hien thi tat ca du an\n";
        cout << "4. tim kiem du an bang ID\n";
        cout << "5. Thoat\n";
        cout << "Choose: ";
        cin >> choice;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        switch (choice) {
            case 1: {
                string id = inputLine("nhap ma du an: ");
                string name = inputLine("nhap ten du an: ");
                string managerId = inputLine("nhap ma quan ly: ");
                string managerName = inputLine("nhap ten quan ly: ");
                string managerRole = inputLine("nhap chuc vu quan ly: ");

                User manager(managerId, managerName, managerRole);
                Project p(id, name, manager);
                app.addProject(p);

                cout << "Du an da duoc them thanh cong  .\n";
                break;
            }

            case 2: {
                string projectId = inputLine("nhap ma du an: ");
                string taskId = inputLine("nhap ma cong viec: ");
                string title = inputLine("nhap ten cong viec: ");
                string status = inputLine("nhap trang thai cong viec: ");
                string deadline = inputLine("nhap han hoan thanh: ");

                Task task(taskId, title, status, deadline);
                app.addTaskToProject(projectId, task);
                break;
            }

            case 3:
                app.displayProjects();
                break;

            case 4: {
                string id = inputLine("nhap ma du an de tim kiem: ");
                app.findProject(id);
                break;
            }

            case 5:
                cout << "Exiting program...\n";
                break;

            default:
                cout << "Invalid choice!\n";
                break;
        }
    } while (choice != 5);

    return 0;
}