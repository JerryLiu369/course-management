/**
 * v0 by Vercel.
 * @see https://v0.dev/t/vCa2j40XoTR
 */
import { Inter } from 'next/font/google'
import '../app/globals.css'
const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: '专业模块',
}

import Link from "next/link"
import { Button } from "@/components/ui/button"
import { CollapsibleTrigger, CollapsibleContent, Collapsible } from "@/components/ui/collapsible"
import { Checkbox } from "@/components/ui/checkbox"
import { TableHead, TableRow, TableHeader, TableCell, TableBody, Table } from "@/components/ui/table"

export default function Component() {
  return (
      <div key="1" className="grid min-h-screen w-full grid-cols-[280px_1fr]">
        <nav className="hidden border-r bg-gray-100/40 lg:block dark:bg-gray-800/40">
          <div className="flex h-full max-h-screen flex-col gap-2">
            <div className="flex h-[60px] items-center border-b px-6">
              <Link className="flex items-center gap-2 font-semibold" href="general">
                <BookOpenIcon className="h-6 w-6"/>
                <span>培养方案制定工具 </span>
              </Link>
            </div>
            <div className="flex-1 overflow-auto py-2">
              <nav className="grid items-start px-4 text-sm font-medium">
                <Collapsible defaultOpen={true} className="space-y-2">
                  <CollapsibleTrigger
                      className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50">
                    <BookIcon className="h-4 w-4"/>
                    课程库查看
                    <ChevronDownIcon className="h-4 w-4 ml-2"/>
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
                          className="flex items-center gap-3 rounded-lg bg-gray-100 px-3 py-2 text-gray-900 transition-all hover:text-gray-900 dark:bg-gray-800 dark:text-gray-50 dark:hover:text-gray-50"
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
        <div className="flex flex-col">
          <main className="flex flex-1 flex-col gap-4 p-4 md:gap-6 md:p-6 relative">
            <div className="flex items-center">
              <h1 className="font-semibold text-lg md:text-2xl">课程</h1>
              <Button className="ml-auto" size="sm" variant="outline">
                <ImportIcon className="w-4 h-4"/>
                <span className="sr-only">从文件导入</span>
              </Button>
              <Button className="ml-2 bg-black text-white" size="sm">
                <Link href="/minus">
                  <MinusIcon className="w-4 h-4"/>
                </Link>
              </Button>
              <Button className="ml-2 bg-black text-white" size="sm">
                <Link href="/add">
                  <PlusIcon className="w-4 h-4"/>
                </Link>
              </Button>
              <Button className="ml-2 bg-black text-white" size="sm">
                课程地图
              </Button>
            </div>
            <div className="flex items-center mb-4">
              <label className="mr-2" htmlFor="majoe">
                专业：
              </label>
              <select className="border rounded px-2 py-1 mr-4" id="major">
                <option>子类一</option>
                <option>子类二</option>
                <option>子类三</option>
              </select>
              <label className="mr-2" htmlFor="category">
                模块：
              </label>
              <select className="border rounded px-2 py-1 mr-4" id="category1">
                <option>子类一</option>
                <option>子类二</option>
                <option>子类三</option>
              </select>
              <select className="border rounded px-2 py-1 mr-4" id="category2">
                <option>子类一</option>
                <option>子类二</option>
                <option>子类三</option>
              </select>
              <Button className="ml-auto bg-black text-white" size="sm">
              确认
              </Button>
            </div>
            <div className="border shadow-sm rounded-lg">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>
                      <Checkbox id="select-all"/>
                    </TableHead>
                    <TableHead>课程名称</TableHead>
                    <TableHead>课程编码</TableHead>
                    <TableHead>课程学分</TableHead>
                    <TableHead>开课学期</TableHead>
                    <TableHead>模块小类</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  <TableRow>
                    <TableCell>
                      <Checkbox id="select-1" />
                    </TableCell>
                    <TableCell>数据结构</TableCell>
                    <TableCell>Jane Doe</TableCell>
                    <TableCell>周一 10:00 - 12:00</TableCell>
                    <TableCell>105室</TableCell>
                    <TableCell>Remark</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>
                      <Checkbox id="select-2" />
                    </TableCell>
                    <TableCell>微积分</TableCell>
                    <TableCell>John Smith</TableCell>
                    <TableCell>周二 13:00 - 15:00</TableCell>
                    <TableCell>206室</TableCell>
                    <TableCell>Remark</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>
                      <Checkbox id="select-3" />
                    </TableCell>
                    <TableCell>英国文学</TableCell>
                    <TableCell>Emma Brown</TableCell>
                    <TableCell>周三 09:00 - 11:00</TableCell>
                    <TableCell>307室</TableCell>
                    <TableCell>Remark</TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </div>
            <div className="flex items-center space-x-2">
              <Button className="bg-black text-white" size="sm">
                计算学分
              </Button>
              <span className="text-black">学分结果: 0</span>
            </div>
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


function MinusIcon(props) {
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
      <path d="M5 12h14" />
    </svg>
  )
}


function PlusIcon(props) {
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
      <path d="M5 12h14" />
      <path d="M12 5v14" />
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
