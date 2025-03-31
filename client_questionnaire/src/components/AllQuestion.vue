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
        }
    },
    components: {
        QuestionItem
    },
    
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