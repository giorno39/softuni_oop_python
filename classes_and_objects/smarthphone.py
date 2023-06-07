class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int):
        if self.memory < app_memory:
            return f"Not enough memory to install {app}"
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"

