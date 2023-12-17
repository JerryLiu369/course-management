(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([[504], {
    6234: function (e, s, r) {
        (window.__NEXT_P = window.__NEXT_P || []).push(["/general", function () {
            return r(9238)
        }])
    }, 9238: function (e, s, r) {
        "use strict";
        r.r(s), r.d(s, {
            default: function () {
                return x
            }, metadata: function () {
                return c
            }
        });
        var n = r(5893);
        r(9182);
        var t = r(1664), l = r.n(t), i = r(487), a = r(6217), h = r(8023), d = r(8571);
        let c = {title: "通识模块"};

        function x() {
            return (0, n.jsxs)("div", {
                className: "grid min-h-screen w-full grid-cols-[280px_1fr]", children: [(0, n.jsx)("nav", {
                    className: "hidden border-r bg-gray-100/40 lg:block dark:bg-gray-800/40",
                    children: (0, n.jsxs)("div", {
                        className: "flex h-full max-h-screen flex-col gap-2",
                        children: [(0, n.jsx)("div", {
                            className: "flex h-[60px] items-center border-b px-6",
                            children: (0, n.jsxs)(l(), {
                                className: "flex items-center gap-2 font-semibold",
                                href: "general",
                                children: [(0, n.jsx)(j, {className: "h-6 w-6"}), (0, n.jsx)("span", {children: "培养方案制定工具 "})]
                            })
                        }), (0, n.jsx)("div", {
                            className: "flex-1 overflow-auto py-2", children: (0, n.jsxs)("nav", {
                                className: "grid items-start px-4 text-sm font-medium",
                                children: [(0, n.jsxs)(a.zF, {
                                    defaultOpen: !0,
                                    className: "space-y-2",
                                    children: [(0, n.jsxs)(a.wy, {
                                        className: "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50",
                                        children: [(0, n.jsx)(o, {className: "h-4 w-4"}), "课程库查看", (0, n.jsx)(m, {className: "h-4 w-4 ml-2"})]
                                    }), (0, n.jsx)(a.Fw, {
                                        children: (0, n.jsxs)("div", {
                                            className: "ml-4 space-y-2",
                                            children: [(0, n.jsxs)(l(), {
                                                className: "flex items-center gap-3 rounded-lg bg-gray-100 px-3 py-2 text-gray-900 transition-all hover:text-gray-900 dark:bg-gray-800 dark:text-gray-50 dark:hover:text-gray-50",
                                                href: "general",
                                                children: [(0, n.jsx)(o, {className: "h-4 w-4"}), "通识模块"]
                                            }), (0, n.jsxs)(l(), {
                                                className: "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50",
                                                href: "major",
                                                children: [(0, n.jsx)(f, {className: "h-4 w-4"}), "专业模块"]
                                            })]
                                        })
                                    })]
                                }), (0, n.jsxs)(l(), {
                                    className: "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50",
                                    href: "calculate",
                                    children: [(0, n.jsx)(p, {className: "h-4 w-4"}), "计算学分"]
                                })]
                            })
                        })]
                    })
                }), (0, n.jsx)("div", {
                    className: "flex flex-col", children: (0, n.jsxs)("main", {
                        className: "flex flex-1 flex-col gap-4 p-4 md:gap-6 md:p-6 relative",
                        children: [(0, n.jsxs)("div", {
                            className: "flex items-center",
                            children: [(0, n.jsx)("h1", {
                                className: "font-semibold text-lg md:text-2xl",
                                children: "课程"
                            }), (0, n.jsxs)(i.z, {
                                className: "ml-auto",
                                size: "sm",
                                variant: "outline",
                                children: [(0, n.jsx)(g, {className: "w-4 h-4"}), (0, n.jsx)("span", {
                                    className: "sr-only",
                                    children: "从文件导入"
                                })]
                            }), (0, n.jsx)(i.z, {
                                className: "ml-2 bg-black text-white",
                                size: "sm",
                                children: (0, n.jsx)(l(), {
                                    href: "/minus",
                                    children: (0, n.jsx)(u, {className: "w-4 h-4"})
                                })
                            }), (0, n.jsx)(i.z, {
                                className: "ml-2 bg-black text-white",
                                size: "sm",
                                children: (0, n.jsx)(l(), {
                                    href: "/add",
                                    children: (0, n.jsx)(w, {className: "w-4 h-4"})
                                })
                            }), (0, n.jsx)(i.z, {
                                className: "ml-2 bg-black text-white",
                                size: "sm",
                                children: "课程地图"
                            })]
                        }), (0, n.jsxs)("div", {
                            className: "flex items-center mb-4",
                            children: [(0, n.jsx)("label", {
                                className: "mr-2",
                                htmlFor: "category",
                                children: "模块："
                            }), (0, n.jsxs)("select", {
                                className: "border rounded px-2 py-1 mr-4",
                                id: "category1",
                                children: [(0, n.jsx)("option", {children: "子类一"}), (0, n.jsx)("option", {children: "子类二"}), (0, n.jsx)("option", {children: "子类三"})]
                            }), (0, n.jsxs)("select", {
                                className: "border rounded px-2 py-1 mr-4",
                                id: "category2",
                                children: [(0, n.jsx)("option", {children: "子类一"}), (0, n.jsx)("option", {children: "子类二"}), (0, n.jsx)("option", {children: "子类三"})]
                            }), (0, n.jsx)(i.z, {
                                className: "ml-auto bg-black text-white",
                                size: "sm",
                                children: "确认"
                            })]
                        }), (0, n.jsx)("div", {
                            className: "border shadow-sm rounded-lg", children: (0, n.jsxs)(d.iA, {
                                children: [(0, n.jsx)(d.xD, {children: (0, n.jsxs)(d.SC, {children: [(0, n.jsx)(d.ss, {children: (0, n.jsx)(h.X, {id: "select-all"})}), (0, n.jsx)(d.ss, {children: "课程名称"}), (0, n.jsx)(d.ss, {children: "课程编码"}), (0, n.jsx)(d.ss, {children: "课程学分"}), (0, n.jsx)(d.ss, {children: "开课学期"}), (0, n.jsx)(d.ss, {children: "模块小类"})]})}), (0, n.jsxs)(d.RM, {children: [(0, n.jsxs)(d.SC, {children: [(0, n.jsx)(d.pj, {children: (0, n.jsx)(h.X, {id: "select-1"})}), (0, n.jsx)(d.pj, {children: "数据结构"}), (0, n.jsx)(d.pj, {children: "Jane Doe"}), (0, n.jsx)(d.pj, {children: "周一 10:00 - 12:00"}), (0, n.jsx)(d.pj, {children: "105室"}), (0, n.jsx)(d.pj, {children: "Remark"})]}), (0, n.jsxs)(d.SC, {children: [(0, n.jsx)(d.pj, {children: (0, n.jsx)(h.X, {id: "select-2"})}), (0, n.jsx)(d.pj, {children: "微积分"}), (0, n.jsx)(d.pj, {children: "John Smith"}), (0, n.jsx)(d.pj, {children: "周二 13:00 - 15:00"}), (0, n.jsx)(d.pj, {children: "206室"}), (0, n.jsx)(d.pj, {children: "Remark"})]}), (0, n.jsxs)(d.SC, {children: [(0, n.jsx)(d.pj, {children: (0, n.jsx)(h.X, {id: "select-3"})}), (0, n.jsx)(d.pj, {children: "英国文学"}), (0, n.jsx)(d.pj, {children: "Emma Brown"}), (0, n.jsx)(d.pj, {children: "周三 09:00 - 11:00"}), (0, n.jsx)(d.pj, {children: "307室"}), (0, n.jsx)(d.pj, {children: "Remark"})]})]})]
                            })
                        }), (0, n.jsxs)("div", {
                            className: "flex items-center space-x-2",
                            children: [(0, n.jsx)(i.z, {
                                className: "bg-black text-white",
                                size: "sm",
                                children: "计算学分"
                            }), (0, n.jsx)("span", {className: "text-black", children: "学分结果: 0"})]
                        })]
                    })
                })]
            }, "1")
        }

        function o(e) {
            return (0, n.jsx)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: (0, n.jsx)("path", {d: "M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"})
            })
        }

        function j(e) {
            return (0, n.jsxs)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: [(0, n.jsx)("path", {d: "M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"}), (0, n.jsx)("path", {d: "M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"})]
            })
        }

        function m(e) {
            return (0, n.jsx)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: (0, n.jsx)("path", {d: "m6 9 6 6 6-6"})
            })
        }

        function p(e) {
            return (0, n.jsxs)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: [(0, n.jsx)("rect", {
                    width: "16",
                    height: "20",
                    x: "4",
                    y: "2",
                    rx: "2"
                }), (0, n.jsx)("line", {x1: "8", x2: "16", y1: "6", y2: "6"}), (0, n.jsx)("line", {
                    x1: "16",
                    x2: "16",
                    y1: "14",
                    y2: "18"
                }), (0, n.jsx)("path", {d: "M16 10h.01"}), (0, n.jsx)("path", {d: "M12 10h.01"}), (0, n.jsx)("path", {d: "M8 10h.01"}), (0, n.jsx)("path", {d: "M12 14h.01"}), (0, n.jsx)("path", {d: "M8 14h.01"}), (0, n.jsx)("path", {d: "M12 18h.01"}), (0, n.jsx)("path", {d: "M8 18h.01"})]
            })
        }

        function g(e) {
            return (0, n.jsxs)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: [(0, n.jsx)("path", {d: "M12 3v12"}), (0, n.jsx)("path", {d: "m8 11 4 4 4-4"}), (0, n.jsx)("path", {d: "M8 5H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-4"})]
            })
        }

        function u(e) {
            return (0, n.jsx)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: (0, n.jsx)("path", {d: "M5 12h14"})
            })
        }

        function w(e) {
            return (0, n.jsxs)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: [(0, n.jsx)("path", {d: "M5 12h14"}), (0, n.jsx)("path", {d: "M12 5v14"})]
            })
        }

        function f(e) {
            return (0, n.jsx)("svg", {
                ...e,
                xmlns: "http://www.w3.org/2000/svg",
                width: "24",
                height: "24",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                strokeWidth: "2",
                strokeLinecap: "round",
                strokeLinejoin: "round",
                children: (0, n.jsx)("polygon", {points: "12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"})
            })
        }
    }
}, function (e) {
    e.O(0, [774, 670, 303, 47, 888, 179], function () {
        return e(e.s = 6234)
    }), _N_E = e.O()
}]);