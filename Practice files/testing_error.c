#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*new_string;
	size_t	string_len;

	if (!s1 && !s2)
		return (NULL);
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	string_len = ft_strlen(s1) + ft_strlen(s2) + 1;
	new_string = malloc(sizeof(char) * (string_len));
	if (!new_string)
		return (NULL);
	ft_strlcpy(new_string, s1, string_len);
	ft_strlcat(new_string, s2, string_len);
	return (new_string);
}
int		main()
{
	char	s1[] = "Hello ";
	char	s2[] = "World";
	//char    s3[] = "Hello " ;

//	printf("     My Function : %zu\n" , ft_strlcat(s1, s2, l));
//	printf("Orginal Function : %zu\n" , strlcat(s3, s2, l));
//    printf("New s1 : %s\n" , s1 );
	printf("New String : %s\n" , (ft_strjoin(s1,s2)) );
	

	return (0);
}