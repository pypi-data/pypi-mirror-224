import gitlab
import os
import argparse
from pydantic import Field
from pydantic_settings import BaseSettings





class Settings(BaseSettings):
    GITLAB_URL: str = Field(..., validation_alias="GITLAB_URL")
    GITLAB_TOKEN: str = Field(..., validation_alias="GITLAB_TOKEN")

    @classmethod
    def validate_environment_variables(cls):
        try:
            cls()
        except ValueError as e:
            #print(f"Error: {e}")
            print("\nPlease ensure the following environment variables are set:")
            print("  - GITLAB_URL: URL of your GitLab instance, e.g., https://gitlab.com")
            print("  - GITLAB_TOKEN: Your personal GitLab access token\n")
            print("You can set them using:")
            print("  export GITLAB_URL=https://your-gitlab-url.com")
            print("  export GITLAB_TOKEN=your_token_here\n")
            exit(1)

    




def clone_project(repo_path, checkout_name):
    """
    Clones a repository from GitLab. The repository path must be in the format
    <namespace>/<project_name>.

    :param repo_path:
    :return:
    """

    settings = Settings()
    gl = gitlab.Gitlab(settings.GITLAB_URL, private_token=settings.GITLAB_TOKEN)

    try:
        project = gl.projects.get(repo_path)
        project_url = project.ssh_url_to_repo
        print(project_url)
        os.system(f"git clone {project_url} {checkout_name}")
    except Exception as e:
        print(f"Error cloning project {repo_path}: {e}")
        return

def show_group(namespace,projects):
    """
    Lists all projects in the given gitlab namespace.
    :param namespace:
    :return:
    """
    settings = Settings()
    gl = gitlab.Gitlab(settings.GITLAB_URL, private_token=settings.GITLAB_TOKEN)

    #namespaces = gl.namespaces.list( all=True)
    #for namespace in namespaces:
    #    print(namespace.name)
    groups = gl.groups.list(all=True)
    for group in groups:
        if group.full_path == namespace or namespace == "":
            handle_group(group, depth=0, projects=projects)
def handle_group(g, depth=0, projects=False):
    settings = Settings()
    gl = gitlab.Gitlab(settings.GITLAB_URL, private_token=settings.GITLAB_TOKEN)

    spaces = " " * depth
    print(f"{spaces}|-{g.full_path}")
    if projects:
        projects = g.projects.list(all=True)
        print_projects(projects, depth)
    subgroups = g.subgroups.list(all=True)
    depth += 2
    if len(subgroups) > 0:
        for subgroup in subgroups:
            group = gl.groups.get(subgroup.id)
            handle_group(group, depth, projects)

def print_projects(projects, depth):
    spaces = " " * (depth+2)

    for project in projects:
        print(f"{spaces}|- {project.name},\t{project.path_with_namespace}")

# Creaetes a project in the given namespace
def create_project(namespace, project_name):

    settings = Settings()
    gl = gitlab.Gitlab(settings.GITLAB_URL, private_token=settings.GITLAB_TOKEN)

    try:
        namespace = gl.namespaces.get(namespace)
        project = gl.projects.create({'name': project_name, 'namespace_id': namespace.id})
        print(f"Created project {project_name} in namespace {namespace.name}: {project.ssh_url_to_repo}")
    except Exception as e:
        print(f"Error creating project {project_name}: {e}")
        return



def main():

    Settings.validate_environment_variables()
    settings = Settings()

    parser = argparse.ArgumentParser(description="GitLab utility commands.")
    subparsers = parser.add_subparsers(dest="command")

    clone_parser = subparsers.add_parser('clone', help="Clone a repository.")
    clone_parser.add_argument("path_with_namespace", type=str, help="Path to the repository with namespace.")
    clone_parser.add_argument("-o", "--output", type=str, help="Output directory.")

    group_parser = subparsers.add_parser('group', help="List all projects and subgroups in a group.")
    # accept empty string as default value
    group_parser.add_argument( "namespace", type=str, help="Namespace of the projects.", default="", nargs="?")
    group_parser.add_argument("-p", "--projects", action="store_true", help="List projects in the group.")

    project_parser = subparsers.add_parser('project', help="Create a project in a namespace.")
    create_project_parser = project_parser.add_subparsers(dest="subcommand")
    create_project_parser = create_project_parser.add_parser('create', help="Create a project in a namespace.")
    create_project_parser.add_argument("namespace", type=str, help="Namespace of the project.")
    create_project_parser.add_argument("project_name", type=str, help="Name of the project.")




    args = parser.parse_args()
    try:
        if args.command == "clone":
            clone_project(args.path_with_namespace, args.output)
        elif args.command == "group":
            show_group(args.namespace, args.projects)
        elif args.command == "project":
            namespace = args.namespace
            project_name = args.project_name
            print(namespace, project_name)
            create_project(namespace, project_name)
            #if args.subcommand == "create":
            #    create_project(args.namespace, args.project_name)
        else:
            print("Invalid command. See available commands with 'gl --help'.")
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()

