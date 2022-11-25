from OOP.static_and_class_methods.static_and_class_methods_exercise.project_document_management.category import Category
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_document_management.document import Document
from OOP.static_and_class_methods.static_and_class_methods_exercise.project_document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        current_category = self.get_category_inst(category_id)
        if current_category:
            current_category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = self.get_topic_inst(topic_id)
        if current_topic:
            current_topic.topic = new_topic
            current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        current_doc = self.get_document(document_id)
        if current_doc:
            current_doc.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = self.get_category_inst(category_id)
        if current_category:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = self.get_topic_inst(topic_id)
        if current_topic:
            self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = self.get_document(document_id)
        if current_document:
            self.documents.remove(current_document)

    def __repr__(self):
        final_result = [str(x) for x in self.documents]
        return '\n'.join(final_result)

    # get instance methods
    def get_category_inst(self, category_id):
        current_category = [x for x in self.categories if x.id == category_id]
        if current_category:
            return current_category[0]

    def get_topic_inst(self, topic_id):
        current_topic = [x for x in self.topics if x.id == topic_id]
        if current_topic:
            return current_topic[0]

    def get_document(self, document_id):
        current_doc = [x for x in self.documents if x.id == document_id]
        if current_doc:
            return current_doc[0]



