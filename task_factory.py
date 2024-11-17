class TaskFactory:
    @staticmethod
    def create_task(title, description):
        return {
            "title": title,
            "description": description
        }