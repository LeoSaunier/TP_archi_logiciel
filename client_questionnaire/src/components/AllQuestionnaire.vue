<script>
import QuestionnaireItem from './QuestionnaireItem.vue';
export default{
    props: {
        questionnaires: Array
    },
    methods: {
        selectQuestionnaire(questionnaire) {
            console.log('Selected questionnaire:', questionnaire);
            this.$emit('selectQuestionnaire', questionnaire);
        },
        deleteQuestionnaire: function(questionnaire){
            console.log('Deleted questionnaire:', questionnaire);
            console.log('Deleting questionnaire:', this.questionnaires);
            fetch(questionnaire.uri,{
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "DELETE"
            }).then(response => {
                if (response.ok) {
                    console.log("Questionnaire deleted successfully");
                    this.$emit('questionnaireDeleted', questionnaire);
                } else if (response.status === 404) {
                    console.error("Questionnaire not found");
                } else if (response.status === 403) {
                    console.error("You do not have permission to delete this questionnaire");
                } else if (response.status === 500) {
                    console.error("Server error while deleting questionnaire");
                } else {
                    console.error("Failed to delete questionnaire");
                }
            })
            .catch(error => {
                console.error("Error deleting questionnaire:", error);
            });
        }
    },
    components: {
        QuestionnaireItem
    },
    emits: ['questionnaireDeleted',"selectQuestionnaire"],
}
</script>

<template>
    <ol>
        <QuestionnaireItem
        v-for="questionnaire in questionnaires"
        :questionnaire="questionnaire"
        @selectQuestionnaire="selectQuestionnaire"
        @deleteQuestionnaire="deleteQuestionnaire">
      </QuestionnaireItem>
    </ol>
</template>