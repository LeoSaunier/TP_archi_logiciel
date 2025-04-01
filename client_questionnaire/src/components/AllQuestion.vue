<script>

import { ref } from 'vue';
import QuestionItem from './QuestionItem.vue';

export default {
    props: {
        questions: Array
    },
    methods: {
        addQuestionnaire() {
            console.log("addQuestionnaire");
        },
        deleteQuestion: function(question){
            console.log('Deleted question:', question);
            console.log('Deleting question:', this.questions);
            fetch(question.uri,{
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "DELETE"
            }).then(response => {
                if (response.ok) {
                    console.log("Question deleted successfully");
                    this.$emit('questionDeleted', question);
                } else if (response.status === 404) {
                    console.error("Question not found");
                } else if (response.status === 403) {
                    console.error("You do not have permission to delete this question");
                } else if (response.status === 500) {
                    console.error("Server error while deleting question");
                } else {
                    console.error("Failed to delete question");
                }
            })
            .catch(error => {
                console.error("Error deleting question:", error);
            });
        }
    },
    components: {
        QuestionItem
    },
    emits: ['questionDeleted'],
    
}

</script>


<template>
    <div>
        <ol>
            <QuestionItem
                v-for="question in questions"
                :question="question"
                @deleteQuestion="deleteQuestion">
            </QuestionItem>
        </ol>
    </div>
</template>