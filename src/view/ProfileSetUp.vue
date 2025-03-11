<script setup lang="ts">
import { Input } from '@/components/ui/input'
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import { Separator } from '@/components/ui/separator'


import { Calendar } from '@/components/ui/calendar'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import {
    DateFormatter,
    type DateValue,
    getLocalTimeZone,
} from '@internationalized/date'
import { CalendarIcon } from 'lucide-vue-next'
import { ref } from 'vue'

const df = new DateFormatter('en-US', {
    dateStyle: 'long',
})

const value = ref<DateValue>()


import {
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from '@/components/ui/form'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { toast } from '@/components/ui/toast'

import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import { h } from 'vue'
import * as z from 'zod'

const formSchema = toTypedSchema(z.object({
    type: z.enum(['all', 'mentions', 'none'], {
        required_error: 'You need to select a notification type.',
    }),
}))

const { handleSubmit } = useForm({
    validationSchema: formSchema,
})

const onSubmit = handleSubmit((values) => {
    toast({
        title: 'You submitted the following values:',
        description: h('pre', { class: 'mt-2 w-[340px] rounded-md bg-slate-950 p-4' }, h('code', { class: 'text-white' }, JSON.stringify(values, null, 2))),
    })
})
</script>

<template>
  <div class="flex justify-center p-6 m-4">
    <!-- part one: Personal Information -->
    <div class="w-full max-w-md p-4 space-y-6">
      <!-- Email -->
      <div class="my-3">
        <p class="text-lg font-medium">Enter your email</p>
        <Input type="email" placeholder="Email" class="w-full" />
      </div>

      <!-- Full Name -->
      <div class="my-3">
        <p class="text-lg font-medium">Enter your full name</p>
        <Input type="text" placeholder="Full Name" class="w-full" />
      </div>

      <!-- Age -->
      <div class="my-3">
        <p class="text-lg font-medium">How old are you?</p>
        <Popover>
          <PopoverTrigger as-child>
            <Button
                variant="outline"
                class="w-full justify-start text-left font-normal py-3 px-4 border rounded-md"
                :class="cn('text-muted-foreground', !value && 'text-muted-foreground')"
            >
              <CalendarIcon class="mr-2 h-4 w-4" />
              {{ value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date" }}
            </Button>
          </PopoverTrigger>
          <PopoverContent class="w-auto p-0">
            <Calendar v-model="value" initial-focus />
          </PopoverContent>
        </Popover>
      </div>

      <!-- Gender Selection -->
      <div class="my-3">
        <p class="text-lg font-medium">Choose your gender</p>
        <form @submit="onSubmit" class="space-y-3">
          <FormField v-slot="{ componentField }" type="radio" name="gender">
            <FormItem>
              <FormControl>
                <RadioGroup class="flex flex-col space-y-2" v-bind="componentField">
                  <FormItem class="flex items-center space-x-3">
                    <RadioGroupItem value="male" id="male" />
                    <FormLabel for="male">Male</FormLabel>
                  </FormItem>
                  <FormItem class="flex items-center space-x-3">
                    <RadioGroupItem value="female" id="female" />
                    <FormLabel for="female">Female</FormLabel>
                  </FormItem>
                  <FormItem class="flex items-center space-x-3">
                    <RadioGroupItem value="other" id="other" />
                    <FormLabel for="other">Other</FormLabel>
                  </FormItem>
                </RadioGroup>
              </FormControl>
            </FormItem>
          </FormField>
        </form>
      </div>

      <!-- Education -->
      <div class="my-3">
        <p class="text-lg font-medium">Your education level</p>
        <Select>
          <SelectTrigger>
            <SelectValue placeholder="Select your education" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectLabel>Education Levels</SelectLabel>
              <SelectItem value="highschool">High School</SelectItem>
              <SelectItem value="bachelor">Bachelor's Degree</SelectItem>
              <SelectItem value="master">Master's Degree</SelectItem>
              <SelectItem value="doctorate">Doctorate</SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
    </div>

    <!-- Separator for styling -->
    <Separator orientation="vertical" class="mx-8 h-full bg-gray-300" />

    <!-- part two: Photos Section -->
    <div class="w-full max-w-md p-4 space-y-6">
      <p class="text-lg font-medium">Upload your photos</p>
      <p class="text-sm text-gray-600">Upload 3-5 photos to complete your profile</p>

      <!-- Photo Upload Input -->
      <div class="my-3 space-y-3">
        <FileUpload label="Upload Profile Picture" />
        <FileUpload label="Upload Additional Photo 1" />
        <FileUpload label="Upload Additional Photo 2" />
      </div>

      <!-- Submit Button -->
      <div class="my-6 flex justify-center">
        <Button
            @click="handleSubmit"
            class="w-full py-2 px-4 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none"
        >
          Complete Profile Setup
        </Button>
      </div>
    </div>
  </div>
</template>

<style>
.vertical-separator {
  transform: rotate(90deg); /* Rotate the separator to make it vertical */
  width: 1px;  /* Adjust width */
  height: 100%; /* Adjust height as needed */
}

</style>