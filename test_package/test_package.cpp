#include <boost/date_time/gregorian/gregorian.hpp>
#include <boost/spirit/include/qi_rule.hpp>
#include <boost/pool/pool.hpp>
#include <boost/serialization/detail/stack_constructor.hpp>
#include <boost/thread.hpp>
#include <boost/locale.hpp>

int main()
{
	boost::locale::generator gen;
	boost::gregorian::gregorian_calendar::is_leap_year(2000);
	boost::spirit::qi::rule<char const*> test;
	boost::pool<> p(sizeof(int));
	boost::serialization::detail::stack_allocate<int>();
	boost::thread thread;
}

