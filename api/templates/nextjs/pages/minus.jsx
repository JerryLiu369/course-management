/**
 * v0 by Vercel.
 * @see https://v0.dev/t/aeoNZmemkZ5
 */
import { Inter } from 'next/font/google'
import '../app/globals.css'
const inter = Inter({ subsets: ['latin'] })

export const metadata = {
    title: '加课',
}

import Link from "next/link"
import { Button } from "@/components/ui/button"
import { CollapsibleTrigger, CollapsibleContent, Collapsible } from "@/components/ui/collapsible"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"

export default function Component() {
  return (
    <div key="1" className="grid min-h-screen w-full grid-cols-[280px_1fr]">
      <nav className="hidden border-r bg-gray-100/40 lg:block dark:bg-gray-800/40">
        <div className="flex h-full max-h-screen flex-col gap-2">
          <div className="flex h-[60px] items-center border-b px-6">
            <Link className="flex items-center gap-2 font-semibold" href="#">
              <BookOpenIcon className="h-6 w-6" />
              <span>删除课程</span>
            </Link>
          </div>
          <div className="flex-1 overflow-auto py-2">
            <nav className="grid items-start px-4 text-sm font-medium">
              <Collapsible className="space-y-2">
                <CollapsibleTrigger className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50">
                  <BookIcon className="h-4 w-4" />
                  课程库查看
                  <ChevronDownIcon className="h-4 w-4 ml-2" />
                </CollapsibleTrigger>
                <CollapsibleContent>
                  <div className="ml-4 space-y-2">
                    <Link
                        className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                        href="general"
                    >
                      <BookIcon className="h-4 w-4"/>
                      通识模块
                    </Link>
                    <Link
                        className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                        href="major"
                    >
                      <StarIcon className="h-4 w-4"/>
                      专业模块
                    </Link>
                  </div>
                </CollapsibleContent>
              </Collapsible>
              <Link
                  className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                  href="calculate"
              >
                <CalculatorIcon className="h-4 w-4"/>
                计算学分
              </Link>
            </nav>
          </div>
        </div>
      </nav>
      <div className="flex flex-col bg-gray-100 rounded-lg p-4 shadow-lg justify-start space-y-4">
        <Button className="self-end w-auto px-2 py-2 bg-white text-blue-500 rounded" href="general">
          <Link href="general">
            返回
          </Link>
        </Button>
        <main className="flex flex-col gap-4 mt-0">
          <div className="flex items-center space-x-2">
            <Label className="w-20 text-right" htmlFor="info">
              专业
            </Label>
            <Input className="rounded-md" id="info" placeholder="专业课程请填写此栏"/>
          </div>
          <div className="flex items-center space-x-2">
            <Label className="w-20 text-right" htmlFor="info1">
              课程名称
            </Label>
            <Input className="rounded-md" id="info1" placeholder=""/>
          </div>
          <div className="flex items-center space-x-2">
            <Label className="w-20 text-right" htmlFor="info2">
              课程代码
            </Label>
            <Input className="rounded-md" id="info2" placeholder=""/>
          </div>
          <div className="flex items-center space-x-2">
            <Label className="w-20 text-right" htmlFor="info3">
              课程模块
            </Label>
            <Input className="rounded-md" id="info3" placeholder=""/>
          </div>
          <div className="flex items-center space-x-2">
            <Label className="w-20 text-right" htmlFor="info4">
              课程学分
            </Label>
            <Input className="rounded-md" id="info4" placeholder=""/>
          </div>
          <div className="flex items-center space-x-2">
            <Label className="w-20 text-right" htmlFor="info5">
              模块小类
            </Label>
            <Input className="rounded-md" id="info5" placeholder=""/>
          </div>
          <Button className="self-start w-auto px-2 py-2 bg-black text-white rounded">提交</Button>
        </main>
      </div>
    </div>
  )
}

function BookIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20" />
    </svg>
  )
}


function BookOpenIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
      <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
    </svg>
  )
}


function CalculatorIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <rect width="16" height="20" x="4" y="2" rx="2" />
      <line x1="8" x2="16" y1="6" y2="6" />
      <line x1="16" x2="16" y1="14" y2="18" />
      <path d="M16 10h.01" />
      <path d="M12 10h.01" />
      <path d="M8 10h.01" />
      <path d="M12 14h.01" />
      <path d="M8 14h.01" />
      <path d="M12 18h.01" />
      <path d="M8 18h.01" />
    </svg>
  )
}


function ChevronDownIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m6 9 6 6 6-6" />
    </svg>
  )
}


function ImportIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M12 3v12" />
      <path d="m8 11 4 4 4-4" />
      <path d="M8 5H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-4" />
    </svg>
  )
}


function StarIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
    </svg>
  )
}
