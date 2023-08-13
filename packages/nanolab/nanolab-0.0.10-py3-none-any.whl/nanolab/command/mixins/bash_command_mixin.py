import subprocess
from .base_mixin import CommandMixinBase


class BashCommandMixin(CommandMixinBase):

    def validate(self):
        pass
        # Validation logic for BashCommand

    def execute(self):
        variables = self._get_completed_variables()
        cmd_string = self.command_instance.command_config['command']
        command = cmd_string.format(**variables)

        # Using subprocess.Popen to capture real-time output
        process = subprocess.Popen(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Printing output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        returncode = process.poll()
        if returncode != 0:
            error_output = process.stderr.read()
            print(f"Error executing command: {command}\nError: {error_output.strip()}")
        else:
            # If there's any additional output at the end, capture and print it
            remaining_output = process.stdout.read()
            if remaining_output:
                print(remaining_output.strip())